# src/managers/EventNotificationManager.py

# --- Imports --- #
from typing import Dict, List
from src.models.Event import Event
from src.models.User import User
from src.services.NotificationService import NotificationService

class EventNotificationManager :
    # manager for handling event notifications and observer attachments
    
    def __init__(self) :
        self._user_notification_services: Dict[str, NotificationService] = {}
    
    def get_notification_service(self, user: User) -> NotificationService :
        # get or create notification service for a user
        if user.user_id not in self._user_notification_services:
            self._user_notification_services[user.user_id] = NotificationService(user)
        return self._user_notification_services[user.user_id]
    
    def attach_owner_to_event(self, event: Event, owner: User) -> None :
        # attach event owner's notification service to the event
        notification_service = self.get_notification_service(owner)
        event.attach(notification_service)
        print(f"Attached notification service for owner {owner.name} to event {event.name}")
    
    def attach_participant_to_event(self, event: Event, participant: User) -> None :
        # attach participant's notification service to the event
        notification_service = self.get_notification_service(participant)
        event.attach(notification_service)
        print(f"Attached notification service for participant {participant.name} to event {event.name}")
    
    def attach_all_participants_to_event(self, event: Event, participants: List[User]) -> None :
        # attach all participants' notification services to the event
        for participant in participants:
            self.attach_participant_to_event(event, participant)
    
    def detach_user_from_event(self, event: Event, user: User) -> None :
        # detach user's notification service from the event
        if user.user_id in self._user_notification_services:
            notification_service = self._user_notification_services[user.user_id]
            event.detach(notification_service)
            print(f"Detached notification service for user {user.name} from event {event.name}")