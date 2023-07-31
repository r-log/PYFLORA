import mysql.connector
import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class AppLogic:
    def __init__(self, db_config):
        self.db_config = db_config

    def check_username_exists(self, username):
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        query = 'SELECT COUNT(*) FROM account_info WHERE username = %s'

        try:
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            user_count = result[0]
            return user_count > 0
        except mysql.connector.Error as error:
            print("Error checking username:", error)
        finally:
            cursor.close()
            connection.close()

    def save_user_data(self, username, password, email):
        connection = mysql.connector.connect(**self.db_config)
        cursor = connection.cursor()
        query = 'INSERT INTO account_info (username, hashed_password, email) VALUES (%s, %s, %s)'

        try:
            # Hash the password before saving to the database
            hashed_password = hash_password(password)
            values = (username, hashed_password, email)
            cursor.execute(query, values)
            connection.commit()
            print("Data saved to the database.")
        except mysql.connector.Error as error:
            print("Error saving data:", error)
        finally:
            cursor.close()
            connection.close()

    def test_connection(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            if connection.is_connected():
                print("Connected to the database.")
                connection.close()
            else:
                print("Failed to connect to the database.")
        except mysql.connector.Error as error:
            print("Error connecting to the database:", error)
