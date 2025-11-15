# src/gui/main_window.py

# --- Imports --- #
import customtkinter as ctk
from ..models.User import User
from .club_management import ClubManagementFrame
from .event_management import EventManagementFrame

class MainWindow(ctk.CTkFrame) :
    def __init__(self, parent, user: User, on_logout) :
        super().__init__(parent)
        self.user = user
        self.on_logout = on_logout
        
        self.create_widgets()
    
    def create_widgets(self) :
        # header w/ user info + logout
        header = ctk.CTkFrame(self, height=60)
        header.pack(fill="x", padx=10, pady=10)
        header.pack_propagate(False)
        
        # welcome message w/ user info
        user_info = ctk.CTkFrame(header)
        user_info.pack(side="left", padx=20, pady=10)
        
        welcome_label = ctk.CTkLabel(
            user_info, 
            text=f"Welcome, {self.user.name}", 
            font=ctk.CTkFont(size=18, weight="bold")
        )
        welcome_label.pack(anchor="w")

        role_label = ctk.CTkLabel(
            user_info,
            text=f"Role: {self.user.get_role()}",
            font=ctk.CTkFont(size=14)
        )
        role_label.pack(anchor="w")

        # logout button
        logout_btn = ctk.CTkButton(
            header, 
            text="Logout", 
            command=self.on_logout,
            width=100,
            height=35
        )
        logout_btn.pack(side="right", padx=20, pady=10)
        
        # main content area with tabs
        self.tab_view = ctk.CTkTabview(self)
        self.tab_view.pack(fill="both", expand=True, padx=10, pady=10)
        
        # create tabs
        self.tab_view.add("Clubs")
        self.tab_view.add("Events")
        self.tab_view.add("My Profile")
        
        # Initialize tab content
        self.club_frame = ClubManagementFrame(self.tab_view.tab("Clubs"), self.user)
        self.club_frame.pack(fill="both", expand=True)
        
        self.event_frame = EventManagementFrame(self.tab_view.tab("Events"), self.user)
        self.event_frame.pack(fill="both", expand=True)
        
        self.profile_frame = self.create_profile_frame()
        self.profile_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    def create_profile_frame(self) :
        frame = ctk.CTkFrame(self.tab_view.tab("My Profile"))
        
        # profile header
        header = ctk.CTkLabel(
            frame, 
            text="My Profile", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        header.pack(pady=20)
        
        # user information
        info_frame = ctk.CTkFrame(frame)
        info_frame.pack(fill="x", padx=50, pady=20)
        
        info_text = f""" 
        User ID: {self.user.user_id}
        Name: {self.user.name}
        Email: {self.user.email}
        Role: {self.user.get_role()}
        """
        
        info_label = ctk.CTkLabel(
            info_frame, 
            text=info_text,
            font=ctk.CTkFont(size=14),
            justify="left"
        )
        info_label.pack(pady=20, padx=20)
        
        return frame