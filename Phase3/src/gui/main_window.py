# src/gui/main_window.py

# --- Imports --- #
import customtkinter as ctk
from ..models.User import User

class MainWindow(ctk.CTkFrame) :
    def __init__(self, parent, user: User, on_logout) :
        super().__init__(parent)
        self.user = user
        self.on_logout = on_logout
        
        self.create_widgets()
    
    def create_widgets(self) :
        # header
        header = ctk.CTkFrame(self, height=60)
        header.pack(fill="x", padx=10, pady=10)
        header.pack_propagate(False)
        
        # welcome message
        welcome_label = ctk.CTkLabel(header, text=f"Welcome, {self.user.name} ({self.user.get_role()})", font=ctk.CTkFont(size=18, weight="bold"))
        welcome_label.pack(side="left", padx=20)
        
        # logout button
        logout_btn = ctk.CTkButton(header, text="Logout", command=self.on_logout)
        logout_btn.pack(side="right", padx=20)
        
        # main content area
        content = ctk.CTkFrame(self)
        content.pack(fill="both", expand=True, padx=10, pady=10)
        
        # placeholder for main content
        placeholder = ctk.CTkLabel(content, text="Main Application Content\n\nClubs and Events management will go here", font=ctk.CTkFont(size=16))
        placeholder.pack(expand=True)