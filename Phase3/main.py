# main.py (main application entry point)

import sys
import os

# Add the project root to Python path so we can use absolute imports
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

try :
    from src.gui.app import main
    if __name__ == "__main__" :
        main()
except Exception as e :
    print(f"Error starting application: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")