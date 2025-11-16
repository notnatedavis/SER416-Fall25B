# src/models/Club.py

# --- Imports --- #
from typing import List
from dataclasses import dataclass, field
from src.models.User import User

@dataclass
class Club :
    # club entity representing a user group or organization
    club_id : str
    name : str
    founder : 'User'
    is_approved : bool = False
    members : List['User'] = field(default_factory=list)

    def __post_init__(self) :
        # add founder as first member after initialization
        self.members.append(self.founder)

    def add_member(self, user: 'User') -> bool :
        if user not in self.members :
            self.members.append(user)
            return True
        return False

    def remove_member(self, user: 'User') -> bool :
        if user in self.members and user != self.founder :
            self.members.remove(user)
            return True
        return False

    def request_approval(self) -> None :
        self.is_approved = False  # update!
        # notify staff ?