# src/gui/registration_window.py

# --- Imports --- #
import customtkinter as ctk
from ..services.Registration import Registration

class RegistrationWindow(ctk.CTkFrame) :

    def __init__(self, parent, on_registration_success, on_show_login) :
        super().__init__(parent)
        self.on_registration_success = on_registration_success
        self.on_show_login = on_show_login
        self.registration_service = Registration()
        
        self.create_widgets()
    
    def create_widgets(self) :
        # main container
        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both", padx=50, pady=50)
        
        # title
        title = ctk.CTkLabel(container, text="Create Account", 
                            font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=(0, 30))
        
        # registration frame
        reg_frame = ctk.CTkFrame(container)
        reg_frame.pack(expand=True, fill="both", padx=100, pady=30)
        
        # name
        ctk.CTkLabel(reg_frame, text="Full Name:", font=ctk.CTkFont(size=14)).pack(pady=(20, 5))
        self.name_entry = ctk.CTkEntry(reg_frame, width=300, height=40)
        self.name_entry.pack(pady=(0, 15))
        
        # email
        ctk.CTkLabel(reg_frame, text="Email:", font=ctk.CTkFont(size=14)).pack(pady=(0, 5))
        self.email_entry = ctk.CTkEntry(reg_frame, width=300, height=40)
        self.email_entry.pack(pady=(0, 15))
        
        # password
        ctk.CTkLabel(reg_frame, text="Password:", font=ctk.CTkFont(size=14)).pack(pady=(0, 5))
        self.password_entry = ctk.CTkEntry(reg_frame, width=300, height=40, show="*")
        self.password_entry.pack(pady=(0, 15))
        
        # confirm password
        ctk.CTkLabel(reg_frame, text="Confirm Password:", font=ctk.CTkFont(size=14)).pack(pady=(0, 5))
        self.confirm_password_entry = ctk.CTkEntry(reg_frame, width=300, height=40, show="*")
        self.confirm_password_entry.pack(pady=(0, 25))
        
        # register button
        self.register_button = ctk.CTkButton(reg_frame, text="Register", command=self.attempt_registration, height=45, font=ctk.CTkFont(size=16))
        self.register_button.pack(pady=(0, 15))
        
        # login link
        login_label = ctk.CTkLabel(reg_frame, text="Already have an account? Login here", text_color="light blue", cursor="hand2")
        login_label.pack()
        login_label.bind("<Button-1>", lambda e: self.on_show_login())
        
        # status label
        self.status_label = ctk.CTkLabel(reg_frame, text="", text_color="red")
        self.status_label.pack(pady=(10, 0))
    
    def attempt_registration(self) :
        # attempt to register a new user
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        self.register_button.configure(state="disabled", text="Registering...")
        
        result = self.registration_service.register_user(name, email, password, confirm_password)
        
        if result['success'] :
            self.status_label.configure(text="Registration successful!", text_color="green")
            self.after(1000, lambda: self.on_registration_success(result['user']))
        else :
            self.status_label.configure(text=result['message'])
            self.register_button.configure(state="normal", text="Register")