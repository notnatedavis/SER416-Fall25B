# src/models/EventRegistration.py

# --- Imports --- #
from datetime import datetime
from dataclasses import dataclass
from src.models.User import User
from src.models.Event import Event

@dataclass
class EventRegistration :
    # represents a user's registration for an event
    registration_id: str
    user: 'User'
    event: 'Event'
    registration_date: datetime
    status: str = "confirmed"  # confirmed, cancelled, waitlisted
    
    def cancel_registration(self) -> bool :
        # cancel this event registration
        if self.status == "confirmed" :
            self.status = "cancelled"
            return True
        return False
    
    def confirm_registration(self) -> bool :
        # confirm a waitlisted registration
        if self.status == "waitlisted" :
            self.status = "confirmed"
            return True
        return False