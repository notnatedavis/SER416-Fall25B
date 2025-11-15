# src/utils/Observer.py

# --- Imports --- #
from abc import ABC, abstractmethod

class Observer(ABC) :
    # abstract base class for observers in the observer pattern

    @abstractmethod
    def update(self, event: 'Event') -> None :
        # update method called by observed subject
        # 'Event' is a string ref to avoid circular import
        pass