from database_ops.database import get_connection

def insert_habit(habit, user_id):
    """Inserts habit into the database"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Inserts a new habit record into the 'habits' table with the specified fields
        query = """
            INSERT INTO habits (id, name, description, periodicity, creation_date, user_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        # Executes the INSERT query to add the habit to the database
        # The habit's attributes and the associated user_id are passed as parameters
        cursor.execute(query, (
            habit.id, 
            habit.name, 
            habit.description, 
            habit.periodicity.name, 
            habit.creation_date, 
            user_id))

        # Commits the transaction to persist the changes to the database
        conn.commit()

    except Exception as e:
        print("Error inserting habit:", e)
    finally:
        # Closes connection to the database
        cursor.close()
        conn.close()

def fetch_habit_by_id(habit_id):
    """Fetches habit from the database by its id"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Selects all habit with a specific id
        # Executes the SELECT query to get required habits from the database
        cursor.execute("SELECT * FROM habits WHERE id = %s", (habit_id,))

        # Gets the first habit
        result = cursor.fetchone()
    except Exception as e:
        print("Error fetching habit:", e)
        return
    finally:
        # Disconnects from the database
        cursor.close()
        conn.close()

    return result

def fetch_habit(name, description, periodicity, user_id):
    """Fetches a habit with specified name, description, periodicity, and user id"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Selects all habits with a specific name, description and user_id
        query = "SELECT * FROM habits WHERE name = %s AND description = %s AND periodicity = %s AND user_id = %s"

        # Executes the SELECT query to get required habits from the database
        cursor.execute(query, (name, description, periodicity, user_id))

        # Gets the first habit
        result = cursor.fetchone()
    except Exception as e:
        print("Error fetching habit:", e)
        return
    finally:
        # Disconnects from the database
        cursor.close()
        conn.close()

    return result

def fetch_habits_by_user_id(user_id):
    """Gets all habits that belong to a specific user"""
    try:
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Selects all habits with a speicific user_id
        query = "SELECT * FROM habits WHERE user_id = %s"

        # Executes the SELECT query to get all habits that belong to a specific user
        cursor.execute(query, (user_id,))

        # Gets the habits
        result = cursor.fetchall()
    except Exception as e:
        print("Error fetching habit:", e)
        return
    finally:
        # Disconnect from the database
        cursor.close()
        conn.close()

    return result

def fetch_habits_by_user_id_and_periodicity(user_id, periodicity):
    """Fetches user's habit of the same periodicity"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Selects all habits with a specific user_id and periodicity
        query = "SELECT * FROM habits WHERE user_id = %s AND periodicity = %s"

        # Executes the SELECT query to get required habits from the database
        cursor.execute(query, (user_id, periodicity.name))

        # Gets the first habit
        result = cursor.fetchall()
    except Exception as e:
        print("Error fetching habits:", e)
        return None
    finally:
        # Disconnects from the database
        cursor.close()
        conn.close()

    return result

def delete_habit(habit_id):
    """Deletes habit from the database"""

    try:
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Executes DELETE query from habits table by passing habit's id as a parameter
        cursor.execute("DELETE FROM habits WHERE id = %s", (habit_id,))

        # Commits the transaction to persist the changes to the database
        conn.commit()
    except Exception as e:
        print("Error deleting habit", e)
        return None
    finally:
        # Disconnect from the database
        cursor.close()
        conn.close()