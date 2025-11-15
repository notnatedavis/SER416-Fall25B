# src/services/AuthenticationService.py

# --- Imports --- #
import uuid
import os
from typing import Dict, Optional
from ..models.User import User

class AuthenticationService :
    # singleton service for handling user authentication and sessions

    _instance = None
    _initialized = False

    def __init__(self) :
        # private constructor for singleton pattern
        if AuthenticationService._initialized :
            return
            
        self._sessions : Dict[str, User] = {}  # session_id -> user mapping
        self._users_file = "users.txt" # plain .txt for user storage
        self._ensure_users_file()
        
        AuthenticationService._instance = self
        AuthenticationService._initialized = True
    
    def _ensure_users_file(self) -> None :
        # create users file if it doesn't exist
        if not os.path.exists(self._users_file):
            open(self._users_file, 'w').close()

    def _load_users(self) -> Dict[str, User] :
        # load users from text file
        users = {}
        try :
            with open(self._users_file, 'r') as f :
                for line in f :
                    if line.strip() :
                        parts = line.strip().split('|')
                        if len(parts) == 5 :
                            user_id, name, email, password, is_staff = parts
                            users[email] = User(
                                user_id=user_id,
                                name=name,
                                email=email,
                                password=password,
                                is_staff=(is_staff.lower() == 'true')
                            )
        except FileNotFoundError :
            pass

        return users

    def _save_user(self, user: User) -> None :
        # save user to text file
        with open(self._users_file, 'a') as f:
            f.write(f"{user.user_id}|{user.name}|{user.email}|{user.password}|{user.is_staff}\n")

    def register(self, name: str, email: str, password: str, is_staff: bool = False) -> Optional[User] :
        # register a new user
        users = self._load_users()
        
        if email in users :
            return None  # user already exists
            
        user_id = f"user_{uuid.uuid4().hex[:8]}"
        user = User(user_id=user_id, name=name, email=email, password=password, is_staff=is_staff)
        
        self._save_user(user)
        return user


    @staticmethod
    def get_instance() -> 'AuthenticationService' :
        if AuthenticationService._instance is None :
            AuthenticationService()
        return AuthenticationService._instance

    def login(self, email: str, password: str) -> Optional[User] :
        # authenticate user and create session.
        # mock auth
        users = self._load_users()
        
        if email in users and users[email].password == password :
            user = users[email]
            session_id = f"session_{uuid.uuid4().hex[:8]}"
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