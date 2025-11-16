# src/models/Event.py

# --- Imports --- #
from typing import List, Dict, Any
from datetime import datetime
from dataclasses import dataclass, field
from src.models.User import User
# use string type hint to avoid circular import
from src.utils.EventObserver import EventObserver

@dataclass
class Event :
    # event entity with observer pattern for notifications
    event_id: str
    name: str
    location: str
    date_time: datetime
    is_free: bool
    description: str
    owner_id: str
    participants: List['User'] = field(default_factory=list)
    _observers: List['EventObserver'] = field(default_factory=list)
    # use string type hint ^

    def update_event_details(self, **kwargs: Any) -> None :
        for key, value in kwargs.items() :
            if hasattr(self, key) :
                setattr(self, key, value)
        
        self.notify_observers()

    def add_participant(self, user: 'User') -> bool :
        if user not in self.participants :
            self.participants.append(user)
            self.notify_observers()

            return True
        
        return False

    def remove_participant(self, user: 'User') -> bool :
        if user in self.participants :
            self.participants.remove(user)
            self.notify_observers()

            return True
        
        return False

    def attach(self, observer: 'EventObserver') -> None :
        if observer not in self._observers :
            self._observers.append(observer)

    def detach(self, observer: 'EventObserver') -> None :
        if observer in self._observers :
            self._observers.remove(observer)

    def notify_observers(self) -> None :
        for observer in self._observers :
            observer.update(self)