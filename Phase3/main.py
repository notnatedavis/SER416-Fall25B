# main.py (main application entry point)

import sys
import os

# add src to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try :
    from gui.app import main
    if __name__ == "__main__" :
        main()
except Exception as e :
    print(f"Error starting application: {e}")
    import traceback
    traceback.print_exc()
    input("Press Enter to exit...")