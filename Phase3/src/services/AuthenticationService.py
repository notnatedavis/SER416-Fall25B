# src/services/AuthenticationService.py

# --- Imports --- #
from typing import Dict, Optional
from ..models.User import User

class AuthenticationService :
    # singleton service for handling user authentication and sessions

    _instance = None
    _sessions: Dict[str, User] = {}  # session_id -> user mapping

    def __init__(self):
        # private constructor for singleton pattern
        if AuthenticationService._instance is not None :
            raise Exception("This class is a singleton!")
        else :
            AuthenticationService._instance = self

    @staticmethod
    def get_instance() -> 'AuthenticationService' :
        if AuthenticationService._instance is None :
            AuthenticationService()
        return AuthenticationService._instance

    def login(self, email: str, password: str) -> Optional[User] :
        # authenticate user and create session.
        # mock auth
        if email and password :
            user = User(
                user_id=f"user_{len(self._sessions)}",
                name=email.split('@')[0],
                email=email,
                password=password # demo
            )
            
            session_id = f"session_{len(self._sessions)}"
            self._sessions[session_id] = user
            return user
            
        return None

    def logout(self, session_id: str) -> bool :
        # logout user and remove session.
        if session_id in self._sessions :
            del self._sessions[session_id]
            return True
        return False

    def get_user_by_session(self, session_id: str) -> Optional[User] :
        # get user by session ID
        return self._sessions.get(session_id)