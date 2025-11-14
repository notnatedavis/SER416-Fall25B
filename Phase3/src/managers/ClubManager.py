# src/managers/ClubManager.py

# --- Imports --- #
from typing import List, Optional
from ..models.Club import Club
from ..factories.ClubFactory import ClubFactory
from ..models.User import User

class ClubManager :
    # Manager class for club operations and business logic
    def __init__(self) :
        # Initialize ClubManager with club factory
        self.club_factory = ClubFactory()
        self._clubs: List[Club] = []

    def create_club(self, name: str, founder: User) -> Optional[Club]:
        # Create a new club
        if not name or not founder :
            return None
            
        club = self.club_factory.create_club(name, founder)
        if club :
            self._clubs.append(club)
        return club

    def join_club(self, club_id: str, user: User) -> bool :
        # Add user to a club
        club = self._find_club_by_id(club_id)
        if club and club.is_approved :
            return club.add_member(user)
        return False

    def search_clubs(self, query: str) -> List[Club] :
        # Search clubs by name
        return [club for club in self._clubs if query.lower() in club.name.lower()]

    def _find_club_by_id(self, club_id: str) -> Optional[Club] :
        # Find club by ID
        return next((club for club in self._clubs if club.club_id == club_id), None)