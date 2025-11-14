# src/utils/Observer.py

# --- Imports --- #
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..models.Event import Event

class Observer(ABC) :
    # abstract base class for observers in the observer pattern

    @abstractmethod
    def update(self, event: 'Event') -> None :
        # update method called by observed subject
        pass