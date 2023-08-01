import mysql.connector
import bcrypt
import re


class AppLogic:
    def __init__(self, db_config):
        self.db_config = db_config

    def test_connection(self):
        # Test the database connection
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                print("Connected to the database.")
                connection.close()
            else:
                print("Failed to connect to the database.")
        except mysql.connector.Error as error:
            print("Error connecting to the database:", error)

    def check_username_exists(self, username):
        # Check if the username already exists in the database
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            query = 'SELECT COUNT(*) FROM account_info WHERE username = %s'
            cursor.execute(query, (username,))
            user_count = cursor.fetchone()[0]
            return user_count > 0
        except mysql.connector.Error as error:
            print("Error checking username:", error)
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def is_valid_email(email):
        # Define the regex pattern for a valid email address
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # Use the re.match() function to check if the email matches the pattern
        return bool(re.match(pattern, email))

    @staticmethod
    def hash_password(password):
        # Generate a salt and hash the password using bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def verify_user_credentials(self, username, password):
        # Verify user credentials during login
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        query = 'SELECT hashed_password FROM account_info WHERE username = %s'

        try:
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            if result:
                hashed_password = result[0].encode('utf-8')
                return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        except mysql.connector.Error as error:
            print("Error verifying credentials:", error)
        finally:
            cursor.close()
            connection.close()

        return False

    def save_user_data(self, username, password, email):
        # Save the user data to the database
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            query = 'INSERT INTO account_info (username, hashed_password, email) VALUES (%s, %s, %s)'

            # Hash the password before saving to the database
            hashed_password = self.hash_password(password)

            values = (username, hashed_password, email)
            cursor.execute(query, values)
            connection.commit()
            print("Data saved to the database.")
        except mysql.connector.Error as error:
            print("Error saving data:", error)
        finally:
            cursor.close()
            connection.close()



