from typing import Optional
import logging
from sqlite3 import Error
from .connection import DatabaseConnection


class Schema:
    """Handles database schema creation and updates."""

    def __init__(self):
        """Initialize Schema with database connection and logger."""
        self.db = DatabaseConnection()
        self.logger = logging.getLogger(__name__)

    def create_tables(self) -> bool:
        """
        Create all necessary database tables and indexes if they don't exist.

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()

                # Users table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP,
                    reset_token TEXT,
                    reset_token_expiry TIMESTAMP
                )
                ''')

                # Plants table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS plants (
                    plant_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT NOT NULL,
                    species TEXT,
                    location TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_watered TIMESTAMP,
                    watering_frequency INTEGER,  -- in days
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
                ''')

                # Sensor readings table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS sensor_readings (
                    reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plant_id INTEGER,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    temperature REAL,
                    humidity REAL,
                    soil_moisture REAL,
                    light_level REAL,
                    FOREIGN KEY (plant_id) REFERENCES plants(plant_id)
                )
                ''')

                # Plant care history
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS care_history (
                    history_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plant_id INTEGER,
                    care_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    care_type TEXT,  -- 'water', 'fertilize', 'prune', etc.
                    notes TEXT,
                    FOREIGN KEY (plant_id) REFERENCES plants(plant_id)
                )
                ''')

                # Plant alerts/notifications
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS alerts (
                    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plant_id INTEGER,
                    user_id INTEGER,
                    alert_type TEXT,  -- 'water', 'temperature', 'humidity', etc.
                    message TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_read BOOLEAN DEFAULT 0,
                    FOREIGN KEY (plant_id) REFERENCES plants(plant_id),
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
                ''')

                # Password reset tokens table
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS password_reset_tokens (
                    token_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL,
                    token TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expiry TIMESTAMP NOT NULL,
                    is_valid BOOLEAN DEFAULT 1,
                    FOREIGN KEY (email) REFERENCES users(email)
                )
                ''')

                # Add index for token lookup
                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_reset_tokens 
                ON password_reset_tokens(token, is_valid)
                ''')

                conn.commit()

                # Create indexes after tables
                if not self.create_indexes():
                    self.logger.error("Failed to create indexes")
                    return False

                self.logger.info(
                    "Database schema and indexes created successfully")
                return True

        except Error as e:
            self.logger.error(f"Error creating database schema: {e}")
            return False

    def reset_database(self) -> bool:
        """
        Reset the database by dropping all tables and recreating them.
        WARNING: This will delete all data!

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()

                # Drop all tables
                tables = [
                    'alerts',
                    'care_history',
                    'sensor_readings',
                    'plants',
                    'users'
                ]

                for table in tables:
                    cursor.execute(f"DROP TABLE IF EXISTS {table}")

                conn.commit()
                self.logger.info("Database reset successfully")

                # Recreate tables
                return self.create_tables()

        except Error as e:
            self.logger.error(f"Error resetting database: {e}")
            return False

    def check_database_version(self) -> Optional[str]:
        """
        Get the current database version.

        Returns:
            Optional[str]: Database version or None if not found
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("PRAGMA user_version")
                return cursor.fetchone()[0]
        except Error as e:
            self.logger.error(f"Error checking database version: {e}")
            return None

    def create_indexes(self) -> bool:
        """
        Create indexes for better query performance.

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()

                # Users table indexes
                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_users_username 
                ON users(username)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_users_email 
                ON users(email)
                ''')

                # Plants table indexes
                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_plants_user_id 
                ON plants(user_id)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_plants_species 
                ON plants(species)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_plants_last_watered 
                ON plants(last_watered)
                ''')

                # Sensor readings indexes
                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_readings_plant_id 
                ON sensor_readings(plant_id)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_readings_timestamp 
                ON sensor_readings(timestamp)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_readings_plant_timestamp 
                ON sensor_readings(plant_id, timestamp)
                ''')

                # Care history indexes
                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_care_plant_id 
                ON care_history(plant_id)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_care_date 
                ON care_history(care_date)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_care_type 
                ON care_history(care_type)
                ''')

                # Alerts indexes
                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_alerts_user_id 
                ON alerts(user_id)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_alerts_plant_id 
                ON alerts(plant_id)
                ''')

                cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_alerts_created_unread 
                ON alerts(created_at) WHERE is_read = 0
                ''')

                conn.commit()
                self.logger.info("Database indexes created successfully")
                return True

        except Error as e:
            self.logger.error(f"Error creating database indexes: {e}")
            return False
