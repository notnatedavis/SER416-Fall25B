# src/managers/EventManager.py

# --- Imports --- #
from typing import List, Optional, Dict, Any
from datetime import datetime
from src.models.Event import Event
from src.factories.EventFactory import EventFactory
from src.models.User import User
from src.services.BaseStorageService import BaseStorageService
from src.managers.EventNotificationManager import EventNotificationManager

class EventManager :

    def __init__(self) :
        # initialize EventManager with event factory and storage
        self.event_factory = EventFactory()
        self.storage = BaseStorageService("events.txt")
        self.notification_manager = EventNotificationManager()
        self._events: List[Event] = []
        self._load_events()

    def _load_events(self) -> None :
        # load events from persistent storage
        lines = self.storage.read_all_lines()
        for line in lines :
            try :
                event_data = line.split('|')
                if len(event_data) >= 7 :
                    event_id, name, location, date_time_str, is_free, description, owner_id = event_data[0], event_data[1], event_data[2], event_data[3], event_data[4], event_data[5], event_data[6]
                    
                    # parse datetime
                    date_time = datetime.fromisoformat(date_time_str)
                    
                    event = Event(
                        event_id=event_id,
                        name=name,
                        location=location,
                        date_time=date_time,
                        is_free=is_free.lower() == 'true',
                        description=description,
                        owner_id=owner_id
                    )
                    
                    # Load participants if available
                    if len(event_data) > 7 and event_data[7] : 
                        participant_ids = event_data[7].split(',')
                        for participant_id in participant_ids:
                            if participant_id :  # skip empty participant IDs
                                participant = User(
                                    user_id=participant_id,
                                    name=f"User_{participant_id}",
                                    email=f"{participant_id}@example.com",
                                    password="temp"
                                )
                                event.add_participant(participant)
                    
                    self._events.append(event)

            except Exception as e :
                print(f"Error loading event from storage: {e}")

    def _save_events(self) -> None :
        # save all events to persistent storage
        lines = []
        for event in self._events :
            # Extract participant IDs
            participant_ids = [user.user_id for user in event.participants]
            participants_str = ','.join(participant_ids)
            
            line = f"{event.event_id}|{event.name}|{event.location}|{event.date_time.isoformat()}|{event.is_free}|{event.description}|{event.owner_id}|{participants_str}"
            lines.append(line)
        
        self.storage.write_all_lines(lines)

    def create_event(self, event_details: Dict[str, Any], owner: User) -> Optional[Event] :
        # create a new event
        try :
            event = self.event_factory.create_event(event_details, owner)
            if event :
                # attach owner's notification service
                self.notification_manager.attach_owner_to_event(event, owner)
                
                self._events.append(event)
                self._save_events()  # save to persistent storage

                # notify about event creation
                event.notify_observers()

            return event
        
        except (ValueError, TypeError) as e :
            print(f"Event creation failed: {e}")
            return None

    def search_events(self, query: str = None, date: datetime = None) -> List[Event] :
        # search events by name or date
        results = self._events
        
        if query :
            query_lower = query.lower()
            results = [
                event for event in results
                if query_lower in event.name.lower() or 
                   query_lower in event.description.lower()
            ]
        
        if date :
            results = [
                event for event in results
                if event.date_time.date() == date.date()
            ]
            
        return results

    def register_for_event(self, event_id: str, user: User) -> bool :
        # register a user for an event
        event = self._find_event_by_id(event_id)

        if event :
            # attach user's notification service before adding participant
            self.notification_manager.attach_participant_to_event(event, user)

            success = event.add_participant(user)
            if success :
                self._save_events()  # save to persistent storage

                # Send confirmation notification
                print(f"Registration confirmed for {user.name} to event {event.name}")

            return success
        
        return False

    def _find_event_by_id(self, event_id: str) -> Optional[Event] :
        # find event by ID
        return next((event for event in self._events if event.event_id == event_id), None)

    def get_events_by_owner(self, owner_id: str) -> List[Event] :
        # get all events owned by a specific user
        return [event for event in self._events if event.owner_id == owner_id]
    
    def update_event(self, event_id: str, **updates) -> bool :
        # update event details and notify observers
        event = self._find_event_by_id(event_id)
        if event :
            event.update_event_details(**updates)
            self._save_events()  # Save changes to storage
            return True
        
        return False