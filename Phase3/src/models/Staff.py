# src/models/Staff.py

# --- Imports --- #
from src.models.User import User
from src.models.Club import Club
from typing import List

class Staff(User) :
    # staff user with administrative privileges for system management
    def __init__(self, user_id: str, name: str, email: str, password: str):
        # initialize Staff user with administrative privileges
        super().__init__(user_id, name, email, password, is_staff=True)
        self.staff_id = f"staff_{user_id}"

    def approve_new_club(self, club: Club) -> bool :
        # approve a new club for activation
        if not club.is_approved :
            club.is_approved = True
            print(f"Club '{club.name}' approved by staff {self.name}")
            return True
        return False

    def reject_club(self, club: Club, reason: str = "") -> bool :
        # reject a club application
        club.is_approved = False
        print(f"Club '{club.name}' rejected by staff {self.name}. Reason: {reason}")
        return True

    def get_pending_clubs(self, clubs: List[Club]) -> List[Club] :
        # get list of clubs pending approval
        return [club for club in clubs if not club.is_approved]