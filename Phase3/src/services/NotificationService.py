# src/services/NotificationService.py

# --- Imports --- #
from ..utils.Observer import Observer
from ..models.Event import Event, EventObserver
from ..models.User import User

class NotificationService(Observer, EventObserver) :
    # service for handling user notifications via email and push
    # implements both Observer & EventObserver for compatability
    def __init__(self, user: User) :
        # initialize notification service for a user
        self.user = user

    def update(self, event: Event) -> None :
        # handle event updates and send notifications
        self.send_email(event)
        self.push_notification(event)

    def send_email(self, event: Event) -> bool :
        # send email notification about event
        print(f"Email sent to {self.user.email} about event: {event.name}")
        return True

    def push_notification(self, event: Event) -> bool :
        # send push notification about event
        print(f"Push notification sent to {self.user.name} about event: {event.name}")
        return True