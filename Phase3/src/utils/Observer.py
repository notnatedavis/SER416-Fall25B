# src/utils/Observer.py

# --- Imports --- #
from abc import ABC, abstractmethod

class Observer(ABC) :
    # abstract base class for observers in the observer pattern
    # still needed ?

    @abstractmethod
    def update(self, *args, **kwargs) -> None :
        # update method called by observed subject
        pass