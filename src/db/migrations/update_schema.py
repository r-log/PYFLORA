import sqlite3
import os


def update_schema():
    """Update database schema to use 'id' instead of 'user_id'"""
    try:
        # Get the database path
        db_path = os.path.join(os.path.dirname(
            os.path.dirname(os.path.dirname(__file__))), 'pyflora.db')
        print(f"Updating schema for database at: {db_path}")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Begin transaction
        cursor.execute("BEGIN TRANSACTION")

        try:
            # 1. Rename users table
            print("Backing up users table...")
            cursor.execute("""
                CREATE TABLE users_backup (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cursor.execute("INSERT INTO users_backup SELECT * FROM users")
            cursor.execute("DROP TABLE users")
            cursor.execute("ALTER TABLE users_backup RENAME TO users")

            # 2. Update password_reset_tokens table
            print("Updating password_reset_tokens table...")
            cursor.execute("""
                CREATE TABLE password_reset_tokens_new (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    token TEXT UNIQUE NOT NULL,
                    user_id INTEGER REFERENCES users(id),
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    used BOOLEAN DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )
            """)
            cursor.execute(
                "INSERT INTO password_reset_tokens_new SELECT * FROM password_reset_tokens")
            cursor.execute("DROP TABLE password_reset_tokens")
            cursor.execute(
                "ALTER TABLE password_reset_tokens_new RENAME TO password_reset_tokens")

            # Commit changes
            conn.commit()
            print("Schema update completed successfully")

        except Exception as e:
            print(f"Error during migration: {e}")
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()

    except Exception as e:
        print(f"Failed to update schema: {e}")
        raise


if __name__ == "__main__":
    update_schema()
