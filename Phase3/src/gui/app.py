# src/gui/app.py

# --- Imports --- #
import customtkinter as ctk
from src.gui.login_window import LoginWindow
from src.gui.registration_window import RegistrationWindow
from src.gui.main_window import MainWindow
from src.services.AuthenticationService import AuthenticationService

class ClubManagementApp(ctk.CTk) :
    # main application class inherits from CTk

    def __init__(self) :
        super().__init__()

        self.auth_service = AuthenticationService.get_instance()
        self.current_user = None
        self.current_frame = None
        
        # configure appearance
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        self.title("Club Management System")
        self.geometry("1200x800")
        
        self.show_login()
    
    def clear_current_frame(self) :
        # clear the current frame from the window
        if self.current_frame :
            self.current_frame.destroy()
            self.current_frame = None
    
    def show_login(self) :
        # show login window
        self.clear_current_frame()
        self.current_frame = LoginWindow(
            self,  # self is now the parent window
            on_login_success=self.on_login_success,
            on_show_register=self.show_registration
        )
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    def show_registration(self) :
        # show registration window
        self.clear_current_frame()
        self.current_frame = RegistrationWindow(
            self,
            on_registration_success=self.on_registration_success,
            on_show_login=self.show_login
        )
        self.current_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    def show_main_window(self) :
        # show main application window
        self.clear_current_frame()
        self.current_frame = MainWindow(
            self,
            user=self.current_user,
            on_logout=self.on_logout
        )
        self.current_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    def on_login_success(self, user) :
        # handle successful login
        self.current_user = user
        self.show_main_window()
    
    def on_registration_success(self, user) :
        # handle successful registration
        self.current_user = user
        self.show_main_window()
    
    def on_logout(self) :
        # handle logout
        self.current_user = None
        self.show_login()
    
def main() :
    # create and run the application
    app = ClubManagementApp()
    app.mainloop()

if __name__ == "__main__" :
    main()