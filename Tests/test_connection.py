import pytest
from database_ops.database import get_connection

def test_db_connection():
    """Tests whether a connection to the database can be successfully established."""

    try:
        # Establish connection to the database
        conn = get_connection()

        # Create a cursor and execute a simple query to check the connection
        with conn.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            db = cursor.fetchone()

            # Assert that a database name is returned
            assert db is not None
            assert db["DATABASE()"] == "habit_tracker"
    except Exception as e:
        # Fail the test if any exception occurs
        pytest.fail(f"Database connection failed: {e}")
    finally:
        # Ensure the connection is closed after the test
        if conn:
            conn.close()