import uuid
from database_ops.database import get_connection

def insert_completion_date(habit, completed_on):
    """Inserts habit completion date into the database"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Inserts a new habit completion date record into the 'habit_completions' table with the specified fields
        query = """
            INSERT INTO habit_completions (id, completed_on, habit_id)
            VALUES (%s, %s, %s)
        """

        # Create an id for completion date
        completion_id = str(uuid.uuid4())

        # Executes the INSERT query to add the habit completion to the database
        # The habit completion's attributes and the associated user_id are passed as parameters
        cursor.execute(query, (
            completion_id, 
            completed_on, 
            habit.id))

        # Commits the transaction to persist the changes to the database
        conn.commit()

    except Exception as e:
        print("Error inserting habit completion:", e)
    finally:
        # Closes connection to the database
        cursor.close()
        conn.close()

    return completion_id

def fetch_completion_date(completion_id):
    """Fetches a habit with specified name, description, periodicity, and user id"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Selects all habits with a specific name, description and user_id
        query = "SELECT * FROM habit_completions WHERE id = %s"

        # Executes the SELECT query to get required habits from the database
        cursor.execute(query, (completion_id,))

        # Gets the first habit
        result = cursor.fetchone()
    except Exception as e:
        print("Error fetching habit completion:", e)
        return
    finally:
        # Disconnects from the database
        cursor.close()
        conn.close()

    return result

def fetch_all_completions(habit_id):
    """Fetches all completions for a specific habit"""

    try:
        # Connects to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Selects all completions with a specific habit_id
        query = "SELECT * FROM habit_completions WHERE habit_id = %s"

        # Executes the SELECT query to get required habits from the database
        cursor.execute(query, (habit_id,))

        # Gets all habit's completions
        result = cursor.fetchall()
    except Exception as e:
        print("Error fetching habit's completions:", e)
        return
    finally:
        # Disconnects from the database
        cursor.close()
        conn.close()

    return result

def delete_completion(completion_id):
    """Deletes habit completion from the database"""

    try:
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Executes DELETE query from habit_completions table by passing habit completion's id as a parameter
        cursor.execute("DELETE FROM habit_completions WHERE id = %s", (completion_id,))

        # Commits the transaction to persist the changes to the database
        conn.commit()
    except Exception as e:
        print("Error deleting habit completion", e)
        return
    finally:
        # Disconnect from the database
        cursor.close()
        conn.close()