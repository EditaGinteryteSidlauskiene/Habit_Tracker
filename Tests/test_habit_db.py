import pytest
from models.habit import Habit
from models.user import User
from enums import Periodicity
from datetime import date
from database_ops.habit_repository import insert_habit, fetch_habits_by_user_id, delete_habit, fetch_habit_by_id, fetch_habit, fetch_habits_by_user_id_and_periodicity
from database_ops.user_repository import fetch_user

@pytest.fixture
def test_habit():
    """Test habit is created to be used for testings"""

    return Habit("Drink water", "At least 8 glasses a day", Periodicity.DAILY)

@pytest.fixture
def user_from_db():
    """Gets an existing user from the database to be used for testing"""

    # Gets user from the database
    user_from_db = fetch_user("William", "william")

    # Create a user object with user's from db data
    user = User(
        name = user_from_db["name"],
        email = user_from_db["email"],
        password = user_from_db["password"])

    # Assign the user ID from DB to the object
    user.id = user_from_db["id"]
    return user

def test_habit_insertion_and_fetching(test_habit, user_from_db):
    """Tests habit insertion and fetching by it name, description, periodicity, and user_id"""

    # Inserts habit into the database
    insert_habit(test_habit, user_from_db.id)

    # Get the habit from database
    habit_from_db = fetch_habit(test_habit.name, test_habit.description, test_habit.periodicity.name, user_from_db.id)
    assert habit_from_db is not None
    assert habit_from_db["id"] == test_habit.id
    assert habit_from_db["name"] ==  test_habit.name
    assert habit_from_db["description"] == test_habit.description
    assert habit_from_db["periodicity"] == test_habit.periodicity.name
    assert habit_from_db["creation_date"].date() == date.today()

    # Deletes the test habit as it is not needed anymore
    delete_habit(test_habit.id)

def test_fetching_habit_by_id(test_habit, user_from_db):
    """Tests fetching habit by its id"""

    # Insert test habit so there would be what to fetch
    insert_habit(test_habit, user_from_db.id)

    # Get inserted test habit from the database
    user_habit_from_db = fetch_habit_by_id(test_habit.id)

    # Checks if the habit fetched by its id is not None
    assert user_habit_from_db is not None

    # Deletes inserted test habit
    delete_habit(test_habit.id)

def test_fetching_habits_by_user_id_and_periodicity(user_from_db, test_habit):
    """Tests fetching user's habits by their periodicity"""

    # Insert a habit so it would be possible to check if it is fecthed
    insert_habit(test_habit, user_from_db.id)

    # Fetch all user's habits with daily periodicity
    habits_from_db = fetch_habits_by_user_id_and_periodicity(user_from_db.id, Periodicity.DAILY)

    # Check if any habits were fetched and if the inserted habit if fecthed
    assert habits_from_db is not None
    assert any(h["id"] == test_habit.id for h in habits_from_db)

    # Delete inserted habit
    delete_habit(test_habit.id)
    
def test_fetching_habits_by_user_id(test_habit, user_from_db):
    """Tests habits fetching by user id"""

    # Insert test habit so there would be what to fetch
    insert_habit(test_habit, user_from_db.id)

    # Get inserted test habit from the database
    user_habits_from_db = fetch_habits_by_user_id(user_from_db.id)

    # Check if fetched any habit
    assert user_habits_from_db is not None

    # Delete test habit
    delete_habit(test_habit.id)