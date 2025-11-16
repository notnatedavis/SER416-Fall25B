# src/gui/login_window.py

# --- Imports --- #
import customtkinter as ctk
from src.services.Login import Login

class LoginWindow(ctk.CTkFrame) :

    def __init__(self, parent, on_login_success, on_show_register) :
        super().__init__(parent)
        
        self.on_login_success = on_login_success
        self.on_show_register = on_show_register
        self.login_service = Login()
        
        self.create_widgets()
    
    def create_widgets(self) :
        # main container
        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both", padx=50, pady=50)
        
        # title
        title = ctk.CTkLabel(container, text="Club Management System", font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=(0, 30))
        
        # login frame
        login_frame = ctk.CTkFrame(container)
        login_frame.pack(expand=True, fill="both", padx=100, pady=50)
        
        # email
        ctk.CTkLabel(login_frame, text="Email:", font=ctk.CTkFont(size=14)).pack(pady=(20, 5))
        self.email_entry = ctk.CTkEntry(login_frame, width=300, height=40)
        self.email_entry.pack(pady=(0, 15))
        
        # password
        ctk.CTkLabel(login_frame, text="Password:", font=ctk.CTkFont(size=14)).pack(pady=(0, 5))
        self.password_entry = ctk.CTkEntry(login_frame, width=300, height=40, show="*")
        self.password_entry.pack(pady=(0, 25))
        
        # login button
        self.login_button = ctk.CTkButton(login_frame, text="Login", command=self.attempt_login, height=45, font=ctk.CTkFont(size=16))
        self.login_button.pack(pady=(0, 15))
        
        # register link
        register_label = ctk.CTkLabel(login_frame, text="Don't have an account? Register here", text_color="light blue", cursor="hand2")
        register_label.pack()
        register_label.bind("<Button-1>", lambda e: self.on_show_register())
        
        # status label
        self.status_label = ctk.CTkLabel(login_frame, text="", text_color="red")
        self.status_label.pack(pady=(10, 0))
    
    def attempt_login(self) :
        # attempt to login with provided credentials
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        
        if not email or not password :
            self.status_label.configure(text="Please enter both email and password")
            return
        
        self.login_button.configure(state="disabled", text="Logging in...")
        
        result = self.login_service.validate_credentials(email, password)
        
        if result['success'] :
            self.status_label.configure(text="Login successful!", text_color="green")
            self.after(1000, lambda: self.on_login_success(result['user']))
        else :
            self.status_label.configure(text=result['message'])
            self.login_button.configure(state="normal", text="Login")