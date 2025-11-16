# src/factories/ClubFactory.py

# --- Imports --- #
import uuid
from src.models.Club import Club
from src.models.User import User

class ClubFactory :
    # factory class for creating Club instances with proper initialization
    def create_club(self, name: str, founder: User) -> Club :
        # create a new Club instance
        if not name or not name.strip() :
            raise ValueError("Club name cannot be empty")
            
        if not founder :
            raise ValueError("Club founder is required")
            
        club_id = f"club_{uuid.uuid4().hex[:8]}"
        return Club(club_id=club_id, name=name.strip(), founder=founder)