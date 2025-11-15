# src/gui/club_management.py

# --- Imports --- #
import customtkinter as ctk
from tkinter import messagebox
from ..managers.ClubManager import ClubManager
from ..models.User import User

class ClubManagementFrame(ctk.CTkFrame) :

    def __init__(self, parent, user: User) :
        super().__init__(parent)

        self.user = user
        self.club_manager = ClubManager()
        
        self.create_widgets()
        self.refresh_clubs_list()
    
    def create_widgets(self) : 
        # main container with two columns
        main_container = ctk.CTkFrame(self)
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # left column - Create club
        left_frame = ctk.CTkFrame(main_container)
        left_frame.pack(side="left", fill="y", padx=(0, 5), pady=10)
        
        # right column - Clubs list
        right_frame = ctk.CTkFrame(main_container)
        right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0), pady=10)
        
        self.setup_create_club_section(left_frame)
        self.setup_clubs_list_section(right_frame)
    
    def setup_create_club_section(self, parent) :
        # create club section
        create_label = ctk.CTkLabel(
            parent, 
            text="Create New Club",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        create_label.pack(pady=10)
        
        # club name input
        name_frame = ctk.CTkFrame(parent)
        name_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(name_frame, text="Club Name:").pack(anchor="w")
        self.club_name_entry = ctk.CTkEntry(name_frame, placeholder_text="Enter club name")
        self.club_name_entry.pack(fill="x", pady=5)
        
        # create button
        create_btn = ctk.CTkButton(
            parent,
            text="Create Club",
            command=self.create_club,
            height=40
        )
        create_btn.pack(pady=10)
        
        # status label
        self.create_status_label = ctk.CTkLabel(parent, text="", text_color="green")
        self.create_status_label.pack()
    
    def setup_clubs_list_section(self, parent) :
        # clubs list section
        list_label = ctk.CTkLabel(
            parent, 
            text="Available Clubs",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        list_label.pack(pady=10)
        
        # search frame
        search_frame = ctk.CTkFrame(parent)
        search_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(search_frame, text="Search:").pack(anchor="w")
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search clubs...")
        self.search_entry.pack(fill="x", pady=5)
        self.search_entry.bind("<KeyRelease>", self.on_search)
        
        # clubs list container
        list_container = ctk.CTkFrame(parent)
        list_container.pack(fill="both", expand=True, padx=10, pady=5)
        
        # clubs list with scrollbar
        self.clubs_listbox = ctk.CTkTextbox(
            list_container, 
            state="disabled",
            wrap="word"
        )
        self.clubs_listbox.pack(fill="both", expand=True, side="left")
        
        # action buttons frame
        action_frame = ctk.CTkFrame(parent)
        action_frame.pack(fill="x", padx=10, pady=5)
        
        refresh_btn = ctk.CTkButton(
            action_frame,
            text="Refresh List",
            command=self.refresh_clubs_list
        )
        refresh_btn.pack(side="left", padx=5)
        
        join_btn = ctk.CTkButton(
            action_frame,
            text="Join Selected Club",
            command=self.join_selected_club
        )
        join_btn.pack(side="right", padx=5)
    
    def create_club(self) :
        club_name = self.club_name_entry.get().strip()
        
        if not club_name :
            messagebox.showerror("Error", "Please enter a club name")
            return
        
        try :
            club = self.club_manager.create_club(club_name, self.user)
            if club :
                self.create_status_label.configure(
                    text=f"Club '{club_name}' created successfully!",
                    text_color="green"
                )
                self.club_name_entry.delete(0, 'end')
                self.refresh_clubs_list()
            else :
                self.create_status_label.configure(
                    text="Failed to create club",
                    text_color="red"
                )
        except Exception as e :
            messagebox.showerror("Error", f"Failed to create club: {str(e)}")
    
    def refresh_clubs_list(self) :
        clubs = self.club_manager.search_clubs("")
        self.display_clubs(clubs)
    
    def display_clubs(self, clubs) : 
        self.clubs_listbox.configure(state="normal")
        self.clubs_listbox.delete("1.0", "end")
        
        if not clubs :
            self.clubs_listbox.insert("end", "No clubs found")
        else :
            for i, club in enumerate(clubs) : 
                status = "Approved" if club.is_approved else "Pending"
                members_count = len(club.members)
                
                # aesthetic print
                club_info = f"""
┌─ Club: {club.name}
│  ID: {club.club_id}
│  Status: {status}
│  Members: {members_count}
│  Founder: {club.founder.name}
└────────────────────────────
"""
                self.clubs_listbox.insert("end", club_info)
        
        self.clubs_listbox.configure(state="disabled")
    
    def on_search(self, event) :
        query = self.search_entry.get().strip()
        clubs = self.club_manager.search_clubs(query)
        self.display_clubs(clubs)
    
    def join_selected_club(self) :
        # for simplicity, join first club in list
        # in real app, have proper selection
        clubs = self.club_manager.search_clubs("")
        if clubs :
            # join the first club as example
            success = self.club_manager.join_club(clubs[0].club_id, self.user)
            if success :
                messagebox.showinfo("Success", f"Joined {clubs[0].name}!")
                self.refresh_clubs_list()
            else :
                messagebox.showerror("Error", "Failed to join club")