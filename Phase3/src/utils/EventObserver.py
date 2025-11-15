# src/utils/EventObserver.py

# --- Imports --- #
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING :
    from ..models.Event import Event

class EventObserver(ABC):
    # abstract base class for event observers
    
    @abstractmethod
    def update(self, event: 'Event') -> None :
        # update method called when observed event changes
        pass
