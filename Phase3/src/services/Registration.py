# src/services/Registration.py

# --- Imports --- #
from .AuthenticationService import AuthenticationService
from ..models.User import User

class Registration :

    def __init__(self) :
        self.auth_service = AuthenticationService.get_instance() # get singleton instance

    def register_user(self, name: str, email: str, password: str, confirm_password: str, is_staff: bool = False) -> dict :
        # register a new user with validation
        if not all([name, email, password, confirm_password]) :
            return {
                'success': False,
                'message': 'All fields are required',
                'user': None
            }
        
        if password != confirm_password :
            return {
                'success': False,
                'message': 'Passwords do not match',
                'user': None
            }
        
        if len(password) < 6 :
            return {
                'success': False,
                'message': 'Password must be at least 6 characters',
                'user': None
            }
        
        try :
            # use instance method properly
            user = self.auth_service.register(name, email, password, is_staff)
            if user :
                return {
                    'success': True,
                    'message': 'Registration successful',
                    'user': user
                }
            else :
                return {
                    'success': False,
                    'message': 'Email already exists',
                    'user': None
                }
            
        except Exception as e :
            return {
                'success': False,
                'message': f'Registration error: {str(e)}',
                'user': None
            }