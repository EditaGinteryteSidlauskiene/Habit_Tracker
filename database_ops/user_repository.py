
from database_ops.database import get_connection

def insert_user(user):
    """Inserts user into the database"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Inserts a new user record into the 'users' table with the specified fields
        query = """
            INSERT INTO users (id, name, email, password)
            VALUES (%s, %s, %s, %s)
        """

        # Executes the INSERT query to add the user to the database
        # The user's attributes are passed as parameters
        cursor.execute(query, (user.id, user.name, user.email, user.password))

        # Commits the transaction to persist the changes to the database
        conn.commit()
    except Exception as e:
        print("Error while inserting user:", e)
        return None
    finally:
        # Closes connection to the database
        cursor.close()          
        conn.close()

def fetch_user(user_name, user_password):
    """Fetches a user from the database by its name and password"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Selects all users with a specific name and password
        query = "SELECT * FROM users WHERE name = %s AND password = %s"

        # Executes the SELECT query to get required users from the database
        cursor.execute(query, (user_name, user_password))

        # Gets the first user
        result = cursor.fetchone()
    except Exception as e:
        print("Error fetching user", e)
        return None
    finally:
        # Disconnects from the database
        cursor.close()
        conn.close()

    return result

def delete_user(user_id):
    """Deletes user from the database by its id"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Deletes a user whose id is passed as a parameter
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))

        # Commits the transaction to persist the changes to the database
        conn.commit()
    except Exception as e:
        print("Error deleting user", e)
        return None
    finally:
        # Disconnects from the database
        cursor.close()
        conn.close()
