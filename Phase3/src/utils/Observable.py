# src/utils/Observable.py

# --- Imports --- #
from typing import List, TYPE_CHECKING
if TYPE_CHECKING :
    from ..utils.Observer import Observer

class Observable :
    # base class for observable objects in the observer pattern
    def __init__(self) :
        # initialize observable with empty observers list
        self.observers: List['Observer'] = []

    def attach(self, observer: 'Observer') -> None :
        # attach an observer to this observable
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer: 'Observer') -> None :
        # detach an observer from this observable
        if observer in self.observers :
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs) -> None :
        # notify all attached observers
        for observer in self.observers :
            observer.update(*args, **kwargs)
