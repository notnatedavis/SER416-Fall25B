# src/managers/EventManager.py

# --- Imports --- #
from typing import List, Optional, Dict, Any
from datetime import datetime
from ..models.Event import Event  # Fixed imports
from ..factories.EventFactory import EventFactory
from ..models.User import User

class EventManager :
    def __init__(self) :
        # initialize EventManager with event factory
        self.event_factory = EventFactory()
        self._events: List[Event] = []

    def create_event(self, event_details: Dict[str, Any], owner: User) -> Optional[Event] :
        # create a new event
        try :
            event = self.event_factory.create_event(event_details, owner)
            self._events.append(event)

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
            return event.add_participant(user)
        
        return False

    def _find_event_by_id(self, event_id: str) -> Optional[Event] :
        # find event by ID
        return next((event for event in self._events if event.event_id == event_id), None)

    def get_events_by_owner(self, owner_id: str) -> List[Event] :
        # get all events owned by a specific user
        return [event for event in self._events if event.owner_id == owner_id]