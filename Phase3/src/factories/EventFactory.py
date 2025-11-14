# src/factories/EventFactory.py

# --- Imports --- #
import uuid
from datetime import datetime
from typing import Dict, Any
from ..models.Event import Event
from ..models.User import User

class EventFactory :
    # factory class for creating Event instances with consistent initialization

    def create_event(self, event_details: Dict[str, Any], owner: User) -> Event :
        # create a new Event instance from event details
        required_fields = ['name', 'location', 'date_time']
        for field in required_fields :
            if field not in event_details or not event_details[field] :
                raise ValueError(f"Missing required field: {field}")
        
        # validate date_time
        if not isinstance(event_details['date_time'], datetime) :
            raise ValueError("date_time must be a datetime object")
        
        event_id = f"event_{uuid.uuid4().hex[:8]}"
        
        return Event(
            event_id=event_id,
            name=event_details['name'].strip(),
            location=event_details['location'].strip(),
            date_time=event_details['date_time'],
            is_free=event_details.get('is_free', True),
            description=event_details.get('description', ''),
            owner_id=owner.user_id
        )