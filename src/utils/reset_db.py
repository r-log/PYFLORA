import os
import sys
from pathlib import Path
from database.schema import Schema


def reset_database():
    # Get the project root directory
    root_dir = Path(__file__).parent.parent.parent
    db_path = root_dir / "my_app.db"

    print(f"Looking for database at: {db_path}")

    if db_path.exists():
        try:
            os.remove(db_path)
            print("Database file deleted successfully!")
        except Exception as e:
            print(f"Error deleting database: {e}")
            return False
    else:
        print("Database file not found - will be created on next app start")

    # Create new database with schema
    try:
        print("Creating new database with schema...")
        schema = Schema()
        if schema.create_tables():
            print("Database created successfully!")
            return True
        else:
            print("Failed to create database schema!")
            return False
    except Exception as e:
        print(f"Error creating database: {e}")
        return False


if __name__ == "__main__":
    reset_database()
