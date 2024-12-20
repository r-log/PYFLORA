import sqlite3
import os
from pathlib import Path
import logging
from typing import Optional


class DatabaseConnection:
    """Database connection handler for SQLite database."""

    def __init__(self):
        """Initialize database connection."""
        # Get path to database file in project root (where main.py is)
        # Navigate up to project root
        root_dir = Path(__file__).parent.parent.parent.parent
        self.db_path = root_dir / "my_app.db"
        print(f"Database path: {self.db_path}")  # Debug print
        self._connection: Optional[sqlite3.Connection] = None
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Setup logging for database operations."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def get_connection(self) -> sqlite3.Connection:
        """
        Get SQLite database connection.

        Returns:
            sqlite3.Connection: Database connection object
        """
        try:
            if not self._connection:
                # Debug print
                print(f"Creating new connection to: {self.db_path}")
                self._connection = sqlite3.connect(str(self.db_path))
                self.logger.info(f"Connected to database: {self.db_path}")
            return self._connection
        except sqlite3.Error as e:
            self.logger.error(f"Error connecting to database: {e}")
            print(f"Connection error: {e}")  # Debug print
            raise

    def close_connection(self) -> None:
        """Close the database connection if it exists."""
        if self._connection:
            try:
                self._connection.close()
                self._connection = None
                self.logger.info("Database connection closed")
            except sqlite3.Error as e:
                self.logger.error(f"Error closing database connection: {e}")
                raise

    def __enter__(self) -> sqlite3.Connection:
        """Context manager entry point."""
        return self.get_connection()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit point."""
        self.close_connection()
