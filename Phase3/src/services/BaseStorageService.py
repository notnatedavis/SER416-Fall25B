# src/services/BaseStorageService.py

# --- Imports --- #
import os
import json
from typing import List, Dict, Any, Optional

class BaseStorageService :
    # Base service for file-based storage operations
    
    def __init__(self, filename: str) :
        self.filename = filename
        self._ensure_file_exists()
    
    def _ensure_file_exists(self) -> None :
        # create file if it doesn't exist
        if not os.path.exists(self.filename) :
            with open(self.filename, 'w') as f :
                f.write("")
    
    def read_all_lines(self) -> List[str]:
        # read all lines from storage file
        try :
            with open(self.filename, 'r') as f :
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError :
            return []
    
    def append_line(self, data: str) -> None :
        # append a line to storage file
        with open(self.filename, 'a') as f :
            f.write(data + '\n')
    
    def write_all_lines(self, lines: List[str]) -> None :
        # write all lines to storage file (overwrite)""
        with open(self.filename, 'w') as f :
            for line in lines :
                f.write(line + '\n')
    
    def clear_file(self) -> None :
        # clear all data from storage file
        with open(self.filename, 'w') as f :
            f.write("")
