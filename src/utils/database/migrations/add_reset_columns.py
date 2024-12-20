import sqlite3


def add_reset_columns():
    try:
        # Connect to database
        # Make sure this path matches your database path
        conn = sqlite3.connect('my_app.db')
        cursor = conn.cursor()

        # Add reset_token column
        cursor.execute('''
            ALTER TABLE users 
            ADD COLUMN reset_token TEXT
        ''')

        # Add reset_token_expiry column
        cursor.execute('''
            ALTER TABLE users 
            ADD COLUMN reset_token_expiry TIMESTAMP
        ''')

        # Commit changes
        conn.commit()
        print("Successfully added reset columns to users table")

    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Columns already exist")
        else:
            print(f"Error adding columns: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    add_reset_columns()
