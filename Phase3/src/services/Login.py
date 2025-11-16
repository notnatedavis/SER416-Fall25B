# src/services/Login.py

# --- Imports --- #
from src.services.AuthenticationService import AuthenticationService
from src.models.User import User

class Login :
    # controller for user login operations and credential validation
    def __init__(self) :
        # initialize Login controller with authentication service
        self.auth_service = AuthenticationService.get_instance()

    def validate_credentials(self, email: str, password: str) -> dict :
        # Validate user credentials and attempt login
        if not email or not password :
            return {
                'success': False,
                'message': 'Email and password are required',
                'user': None
            }
        
        try :
            user = self.auth_service.login(email, password)
            if user :
                return {
                    'success': True,
                    'message': 'Login successful',
                    'user': user
                }
            else :
                return {
                    'success': False,
                    'message': 'Invalid email or password',
                    'user': None
                }
            
        except Exception as e :
            return {
                'success': False,
                'message': f'Login error: {str(e)}',
                'user': None
            }