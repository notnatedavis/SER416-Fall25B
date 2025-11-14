# src/utils/ApplicationConfiguration.py

# --- Imports --- #
import os
import json
from typing import Dict, Any

class ApplicationConfiguration :
    # Singleton class for managing application configuration
    # Ensures consistent configuration access across the application

    _instance = None
    _config: Dict[str, Any] = {}

    def __init__(self) :
        # private constructor for singleton pattern
        if ApplicationConfiguration._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ApplicationConfiguration._instance = self
            self._load_configuration()

    @staticmethod
    def get_instance() -> 'ApplicationConfiguration' :
        if ApplicationConfiguration._instance is None :
            ApplicationConfiguration()
        return ApplicationConfiguration._instance

    def _load_configuration(self) -> None :
        # load configuration from environment and default settings
        # default configuration
        self._config = {
            "database": {
                "host": os.getenv("DB_HOST", "localhost"),
                "port": os.getenv("DB_PORT", "5432"),
                "name": os.getenv("DB_NAME", "club_management"),
            },
            "security": {
                "session_timeout": int(os.getenv("SESSION_TIMEOUT", "3600")),
                "max_login_attempts": int(os.getenv("MAX_LOGIN_ATTEMPTS", "3")),
            },
            "notifications": {
                "enabled": os.getenv("NOTIFICATIONS_ENABLED", "true").lower() == "true",
            }
        }

    def get_property(self, key: str) -> Any :
        keys = key.split('.')
        value = self._config
        
        for k in keys :
            if isinstance(value, dict) and k in value :
                value = value[k]
            else :
                raise KeyError(f"Configuration key '{key}' not found")
                
        return value

    def set_property(self, key: str, value: Any) -> None :
        keys = key.split('.')
        config_ref = self._config
        
        for k in keys[:-1]:
            if k not in config_ref:
                config_ref[k] = {}
            config_ref = config_ref[k]
            
        config_ref[keys[-1]] = value