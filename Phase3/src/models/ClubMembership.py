# src/models/ClubMembership.py

# --- Imports --- #
from datetime import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING
if TYPE_CHECKING :
    from ..models.User import User

@dataclass
class ClubMembership :
    # represents a user's membership in a club with status and metadata
    membership_id: str
    user: 'User'
    club_id: str
    join_date: datetime
    status: str = "active"  # (active, pending, suspended, inactive)
    
    def approve_membership(self) -> bool :
        # approve a pending membership
        if self.status == "pending":
            self.status = "active"
            return True
        
        return False
    
    def suspend_membership(self) -> bool :
        # suspend an active membership
        if self.status == "active" :
            self.status = "suspended"
            return True
        
        return False
    
    def reactivate_membership(self) -> bool :
        # reactivate a suspended membership
        if self.status == "suspended" :
            self.status = "active"
            return True
        
        return False