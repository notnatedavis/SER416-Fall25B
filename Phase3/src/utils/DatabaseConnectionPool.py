# src/utils/DatabaseConnectionPool.py

# --- Imports --- #
import logging
from typing import List, Optional

class DatabaseConnection :
    # mock db connection pool 
    def __init__(self, connection_id: int) :
        self.connection_id = connection_id
        self.is_active = True
        
    def execute(self, query: str) -> bool :
        # execute a database query
        logging.info(f"Connection {self.connection_id} executing: {query}")
        return True
        
    def close(self) -> None :
        # close the connection
        self.is_active = False
        
class DatabaseConnectionPool :
    # singleton connection pool for managing database connections

    _instance = None
    _connections: List[DatabaseConnection] = []
    _max_connections = 10

    def __init__(self) :
        # private constructor for singleton pattern
        if DatabaseConnectionPool._instance is not None :
            raise Exception("This class is a singleton!")
        else :
            DatabaseConnectionPool._instance = self
            self._initialize_connections()

    @staticmethod
    def get_instance() -> 'DatabaseConnectionPool' :
        if DatabaseConnectionPool._instance is None :
            DatabaseConnectionPool()
        return DatabaseConnectionPool._instance

    def _initialize_connections(self) -> None :
        # initialize the connection pool
        try :
            from ..utils.ApplicationConfiguration import ApplicationConfiguration
            
            config = ApplicationConfiguration.get_instance()
            self._max_connections = config.get_property('database.max_connections')
        except (ImportError, KeyError) :
            # use default if config not available
            self._max_connections = 10
        
        for i in range(3) :
            self._connections.append(DatabaseConnection(i))

    def get_connection(self) -> Optional[DatabaseConnection] :
        for conn in self._connections :
            if conn.is_active :
                return conn
        
        # create new connection if pool not full
        if len(self._connections) < self._max_connections :
            new_conn = DatabaseConnection(len(self._connections))
            self._connections.append(new_conn)
            return new_conn
            
        return None

    def close_all_connections(self) -> None :
        # close all connections in the pool
        for conn in self._connections :
            conn.close()
        self._connections.clear()