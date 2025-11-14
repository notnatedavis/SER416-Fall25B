# demo.py
# Demonstration script of system functionality w/ imports

# --- Imports --- #
import sys
import os
from datetime import datetime, timedelta
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from services import AuthenticationService, NotificationService, Login
from managers import ClubManager, EventManager
from factories import ClubFactory, EventFactory
from utils import ValidatePrivileges

def demonstrate_system() :
    """Demonstrate core system functionality with proper imports."""
    print("=== Club Management System Demo ===\n")
    
    # 1. Authentication Demo
    print("1. AUTHENTICATION DEMO")
    auth_service = AuthenticationService.get_instance()
    user = auth_service.login("john@example.com", "password123")
    print(f"✓ User logged in: {user.name} (ID: {user.user_id})")
    
    # 2. Club Creation Demo
    print("\n2. CLUB CREATION DEMO")
    club_manager = ClubManager()
    tech_club = club_manager.create_club("Technology Enthusiasts", user)
    print(f"✓ Club created: {tech_club.name} (ID: {tech_club.club_id})")
    
    # 3. Event System Demo
    print("\n3. EVENT SYSTEM DEMO")
    event_manager = EventManager()
    event_date = datetime.now() + timedelta(days=7)
    
    event_details = {
        'name': 'Python Workshop',
        'location': 'Tech Lab 101',
        'date_time': event_date,
        'is_free': True,
        'description': 'Learn Python programming basics'
    }
    
    tech_event = event_manager.create_event(event_details, user)
    print(f"✓ Event created: {tech_event.name}")
    
    # 4. Notification Demo
    print("\n4. NOTIFICATION SYSTEM DEMO")
    notification_service = NotificationService(user)
    tech_event.attach(notification_service)
    
    # Update event to trigger notification
    tech_event.update_event_details(location="Updated Location")
    print("✓ Event updated - notifications triggered")
    
    # 5. Privilege Check Demo
    print("\n5. PRIVILEGE CHECK DEMO")
    can_manage = ValidatePrivileges.can_manage_event(user, tech_event)
    print(f"✓ User can manage event: {can_manage}")
    
    print("\n=== Demo Completed Successfully ===")

if __name__ == "__main__" :
    demonstrate_system()