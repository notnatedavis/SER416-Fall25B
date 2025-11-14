# src/utils/ValidatePrivileges.py

# --- Imports --- #
from ..models.User import User
from ..models.Event import Event
from ..models.Club import Club

class ValidatePrivileges :
    # utility class for validating user privileges across the system
    @staticmethod
    def can_manage_event(user: User, event: Event) -> bool :
        # check if user can manage (edit/delete) an event
        if not user or not event :
            return False
            
        # event owner can always manage their events
        if user.user_id == event.owner_id :
            return True
            
        # staff users can manage any event
        if user.is_staff :
            return True
            
        return False

    @staticmethod
    def can_manage_club(user: User, club: Club) -> bool :
        # check if user can manage a club
        if not user or not club :
            return False
            
        # club founder can manage the club
        if user.user_id == club.founder.user_id :
            return True
            
        # staff users can manage any club
        if user.is_staff :
            return True
            
        return False

    @staticmethod
    def can_approve_clubs(user: User) -> bool :
        # check if user can approve clubs
        return user and user.is_staff

    @staticmethod
    def can_view_sensitive_data(user: User) -> bool :
        # check if user can view sensitive system data
        return user and user.is_staff