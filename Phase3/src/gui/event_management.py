# src/gui/event_management.py

# --- Imports --- #
import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from src.managers.EventManager import EventManager
from src.models.User import User

class EventManagementFrame(ctk.CTkFrame) :

    def __init__(self, parent, user: User) :
        super().__init__(parent)

        self.user = user
        self.event_manager = EventManager()
        
        self.create_widgets()
        self.refresh_events_list()
    
    def create_widgets(self) :
        # main container with two columns
        main_container = ctk.CTkFrame(self)
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # left column - Create event
        left_frame = ctk.CTkFrame(main_container)
        left_frame.pack(side="left", fill="y", padx=(0, 5), pady=10)
        
        # right column - Events list
        right_frame = ctk.CTkFrame(main_container)
        right_frame.pack(side="right", fill="both", expand=True, padx=(5, 0), pady=10)
        
        self.setup_create_event_section(left_frame)
        self.setup_events_list_section(right_frame)
    
    def setup_create_event_section(self, parent) :
        create_label = ctk.CTkLabel(
            parent, 
            text="Create New Event",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        create_label.pack(pady=10)
        
        # Event form
        form_frame = ctk.CTkFrame(parent)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Event name
        ctk.CTkLabel(form_frame, text="Event Name:").pack(anchor="w", pady=(5,0))
        self.event_name_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter event name")
        self.event_name_entry.pack(fill="x", pady=5)
        
        # Location
        ctk.CTkLabel(form_frame, text="Location:").pack(anchor="w", pady=(5,0))
        self.location_entry = ctk.CTkEntry(form_frame, placeholder_text="Enter location")
        self.location_entry.pack(fill="x", pady=5)
        
        # Date and time
        datetime_frame = ctk.CTkFrame(form_frame)
        datetime_frame.pack(fill="x", pady=5)
        
        ctk.CTkLabel(datetime_frame, text="Date (YYYY-MM-DD):").pack(anchor="w")
        self.date_entry = ctk.CTkEntry(datetime_frame, placeholder_text="2024-01-01")
        self.date_entry.pack(fill="x", pady=2)
        
        ctk.CTkLabel(datetime_frame, text="Time (HH:MM):").pack(anchor="w")
        self.time_entry = ctk.CTkEntry(datetime_frame, placeholder_text="14:30")
        self.time_entry.pack(fill="x", pady=2)
        
        # description
        ctk.CTkLabel(form_frame, text="Description:").pack(anchor="w", pady=(5,0))
        self.description_entry = ctk.CTkTextbox(form_frame, height=60)
        self.description_entry.pack(fill="x", pady=5)
        
        # Free event checkbox
        self.is_free_var = ctk.BooleanVar(value=True)
        free_check = ctk.CTkCheckBox(
            form_frame, 
            text="Free Event", 
            variable=self.is_free_var
        )
        free_check.pack(anchor="w", pady=5)
        
        # create button
        create_btn = ctk.CTkButton(
            parent,
            text="Create Event",
            command=self.create_event,
            height=40
        )
        create_btn.pack(pady=10)
        
        # status label
        self.create_status_label = ctk.CTkLabel(parent, text="", text_color="green")
        self.create_status_label.pack()
    
    def setup_events_list_section(self, parent) :
        list_label = ctk.CTkLabel(
            parent, 
            text="Available Events",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        list_label.pack(pady=10)
        
        # search frame
        search_frame = ctk.CTkFrame(parent)
        search_frame.pack(fill="x", padx=10, pady=5)
        
        ctk.CTkLabel(search_frame, text="Search:").pack(anchor="w")
        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search events...")
        self.search_entry.pack(fill="x", pady=5)
        self.search_entry.bind("<KeyRelease>", self.on_search)
        
        # events list container
        list_container = ctk.CTkFrame(parent)
        list_container.pack(fill="both", expand=True, padx=10, pady=5)
        
        # events list with scrollbar
        self.events_listbox = ctk.CTkTextbox(
            list_container, 
            state="disabled",
            wrap="word"
        )
        self.events_listbox.pack(fill="both", expand=True, side="left")
        
        # action buttons frame
        action_frame = ctk.CTkFrame(parent)
        action_frame.pack(fill="x", padx=10, pady=5)
        
        refresh_btn = ctk.CTkButton(
            action_frame,
            text="Refresh List",
            command=self.refresh_events_list
        )
        refresh_btn.pack(side="left", padx=5)
        
        register_btn = ctk.CTkButton(
            action_frame,
            text="Register for Event",
            command=self.register_for_event
        )
        register_btn.pack(side="right", padx=5)
    
    def create_event(self) :
        event_name = self.event_name_entry.get().strip()
        location = self.location_entry.get().strip()
        date_str = self.date_entry.get().strip()
        time_str = self.time_entry.get().strip()
        description = self.description_entry.get("1.0", "end-1c").strip()
        is_free = self.is_free_var.get()
        
        # validate required fields
        if not all([event_name, location, date_str, time_str]) : 
            messagebox.showerror("Error", "Please fill all required fields")
            return
        
        # parse datetime
        try :
            datetime_str = f"{date_str} {time_str}"
            date_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        except ValueError :
            messagebox.showerror("Error", "Invalid date or time format. Use YYYY-MM-DD and HH:MM")
            return
        
        event_details = {
            'name': event_name,
            'location': location,
            'date_time': date_time,
            'is_free': is_free,
            'description': description
        }
        
        try :
            event = self.event_manager.create_event(event_details, self.user)
            if event :
                self.create_status_label.configure(
                    text=f"Event '{event_name}' created successfully!",
                    text_color="green"
                )
                self.clear_event_form()
                self.refresh_events_list()
            else :
                self.create_status_label.configure(
                    text="Failed to create event",
                    text_color="red"
                )
        except Exception as e :
            messagebox.showerror("Error", f"Failed to create event: {str(e)}")
    
    def clear_event_form(self) :
        self.event_name_entry.delete(0, 'end')
        self.location_entry.delete(0, 'end')
        self.date_entry.delete(0, 'end')
        self.time_entry.delete(0, 'end')
        self.description_entry.delete("1.0", "end")
    
    def refresh_events_list(self) :
        events = self.event_manager.search_events()
        self.display_events(events)
    
    def display_events(self, events) :
        self.events_listbox.configure(state="normal")
        self.events_listbox.delete("1.0", "end")
        
        if not events :
            self.events_listbox.insert("end", "No events found")
        else :
            for event in events :
                free_status = "Free" if event.is_free else "Paid"
                participants_count = len(event.participants)
                
                # aesthetic display
                event_info = f"""
┌─ Event: {event.name}
│  Location: {event.location}
│  Date: {event.date_time.strftime('%Y-%m-%d %H:%M')}
│  Type: {free_status}
│  Participants: {participants_count}
│  Description: {event.description[:50]}...
└────────────────────────────

"""
                self.events_listbox.insert("end", event_info)
        
        self.events_listbox.configure(state="disabled")
    
    def on_search(self, event) :
        query = self.search_entry.get().strip()
        events = self.event_manager.search_events(query)
        self.display_events(events)
    
    def register_for_event(self) :
        events = self.event_manager.search_events("")
        if events :
            # Register for first event as example
            success = self.event_manager.register_for_event(events[0].event_id, self.user)
            if success :
                messagebox.showinfo("Success", f"Registered for {events[0].name}!")
                self.refresh_events_list()
            else :
                messagebox.showerror("Error", "Failed to register for event")