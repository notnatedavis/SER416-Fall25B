# src/models/User.py

# --- Imports --- #
from typing import Optional
from dataclasses import dataclass

@dataclass
class User :
    # user entity representing both regular users and staff members
    user_id : str
    name : str
    email : str
    password : str 
    is_staff : bool = False

    def login(self) -> bool : 
        # authentication logic handled by AuthenticationService
        # update!
        return True

    def get_role(self) -> str :
        return "staff" if self.is_staff else "user"

    def update_profile(self, name: Optional[str] = None, email: Optional[str] = None) -> None :
        if name :
            self.name = name
        if email :
            self.email = email