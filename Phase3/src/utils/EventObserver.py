# src/utils/EventObserver.py

# --- Imports --- #
from abc import ABC, abstractmethod

class EventObserver(ABC) :
    # abstract base class for event observers
    
    @abstractmethod
    def update(self, event: 'Event') -> None :
        # update method called when observed event changes
        pass