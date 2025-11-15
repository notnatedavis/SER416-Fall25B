# src/managers/ClubManager.py

# --- Imports --- #
from typing import List, Optional
from ..models.Club import Club
from ..factories.ClubFactory import ClubFactory
from ..models.User import User
from ..services.BaseStorageService import BaseStorageService
import uuid

class ClubManager :
    # Manager class for club operations and business logic

    def __init__(self) :
        # Initialize ClubManager with club factory & storage
        self.club_factory = ClubFactory()
        self.storage = BaseStorageService("clubs.txt")
        self._clubs: List[Club] = []
        self._load_clubs()

    def _load_clubs(self) -> None :
        # Load clubs from persistent storage
        lines = self.storage.read_all_lines()
        for line in lines :
            try :
                club_data = line.split('|')
                if len(club_data) >= 4 :
                    club_id, name, founder_id, is_approved = club_data[0], club_data[1], club_data[2], club_data[3]
                    
                    # create a temporary founder user (in real app, would lookup from UserService)
                    founder = User(
                        user_id=founder_id,
                        name=f"User_{founder_id}",
                        email=f"{founder_id}@example.com",
                        password="temp"
                    )
                    
                    club = Club(
                        club_id=club_id,
                        name=name,
                        founder=founder,
                        is_approved=is_approved.lower() == 'true'
                    )
                    
                    # load members if available
                    if len(club_data) > 4 and club_data[4] :
                        member_ids = club_data[4].split(',')
                        for member_id in member_ids :
                            if member_id :  # skip empty member IDs
                                member = User(
                                    user_id=member_id,
                                    name=f"User_{member_id}",
                                    email=f"{member_id}@example.com", 
                                    password="temp"
                                )
                                club.add_member(member)
                    
                    self._clubs.append(club)
            except Exception as e :
                print(f"Error loading club from storage: {e}")

    def _save_clubs(self) -> None :
        # save all clubs to persistent storage
        lines = []
        for club in self._clubs :
            # Extract member IDs
            member_ids = [user.user_id for user in club.members]
            members_str = ','.join(member_ids)
            
            line = f"{club.club_id}|{club.name}|{club.founder.user_id}|{club.is_approved}|{members_str}"
            lines.append(line)
        
        self.storage.write_all_lines(lines)

    def create_club(self, name: str, founder: User) -> Optional[Club]:
        # create a new club
        if not name or not founder:
            return None
            
        club = self.club_factory.create_club(name, founder)
        if club:
            self._clubs.append(club)
            self._save_clubs()  # save to persistent storage
        return club

    def join_club(self, club_id: str, user: User) -> bool :
        # add user to a club
        club = self._find_club_by_id(club_id)
        if club and club.is_approved :
            success = club.add_member(user)
            if success :
                self._save_clubs()  # save to persistent storage
            
            return success
        
        return False

    def search_clubs(self, query: str) -> List[Club] :
        # search clubs by name
        return [club for club in self._clubs if query.lower() in club.name.lower()]

    def _find_club_by_id(self, club_id: str) -> Optional[Club] :
        # find club by ID
        return next((club for club in self._clubs if club.club_id == club_id), None)
    
    def approve_club(self, club_id: str) -> bool :
        # approve a club (staff function
        club = self._find_club_by_id(club_id)
        if club :
            club.is_approved = True
            self._save_clubs()  # save to persistent storage
            return True
        
        return False
    
    def get_pending_clubs(self) -> List[Club] :
        # get clubs pending approval
        return [club for club in self._clubs if not club.is_approved]