
import pytest
from models.user import User
from models.habit import Habit
from database_ops.habit_repository import fetch_habit, delete_habit
from database_ops.user_repository import fetch_user
from enums import Periodicity

@pytest.fixture
def test_user():
    """This creates a user object. This user is already in the database and will be used for tests"""

    return User("Mark", "mark@gmail.com", "mark")

@pytest.fixture
def test_user_from_db(test_user):
    """This is the same user, fetched from the database"""

    return fetch_user(test_user.name, test_user.password)

@pytest.fixture
def test_habit():
    """This creates a habit object and will be used for tests. This habit does not exist in the database"""

    return Habit("Eat vegetables", "7 units a day", Periodicity.DAILY)

def test_user_creation():
    """Tests if the user object is created correctly"""

    user = User("A", "a@gmail.com", "pass")
    assert user.name == "A"
    assert user.email == "a@gmail.com"
    assert user.password == "pass"
    assert user.habits == []

def test_user_creation_fails_without_name():
    """Tests if the correct error is thrown when a user is being created without a name"""

    with pytest.raises(ValueError, match="Name cannot be empty."):
        User("", "email@gmail.com", "pass")

def test_user_creation_fails_without_email():
    """Tests if the correct error is thrown when a user is being created without an email"""

    with pytest.raises(ValueError, match="Email cannot be empty."):
        User("Alice", "", "pass")

def test_user_creation_fails_without_password():
    """Tests if the correct error is thrown when a user is being created without a password"""

    with pytest.raises(ValueError, match="Password cannot be empty."):
        User("Alice", "email@gmail.com", "")

def test_user_ids_are_unique():
    """Tests if user ids are unique"""

    user1 = User("A", "a@gmail.com", "pass")
    user2 = User("B", "b@gmail.com", "pass")
    assert user1.id != user2.id

def test_user_fail_with_invalid_email():
    """Tests if the correct error is thrown when a user is being created with invalid email"""

    with pytest.raises(ValueError, match="Email is not valid."):
        User("Alice", "email.gmail.com", "pass")

def test_adding_habit(test_user, test_habit, test_user_from_db):
    """Tests if a habit is correctly added into user's habits list"""

    test_user.id = test_user_from_db["id"]
    # Adds a habit into user's habits list
    test_user.add_habit(test_habit)

    # Checks if the user's habits list is not empty and the added habit is in this list
    assert test_user.habits != []
    assert test_habit in test_user.habits

    # Checks if the habit was inserted into the database and assigned to a specific user
    # 1. Fetch a specific habit that belongs to a specific user from the database
    habit_from_db = fetch_habit(test_habit.name, test_habit.description, test_habit.periodicity.name, test_user.id)
    # 2. Check if the habit was fetched
    assert habit_from_db is not None
    # 3. Check if user_id the habit holds and user's id are the same
    assert habit_from_db["user_id"] == test_user.id

    # Deletes added habit, because it was added for testing only
    test_user.delete_habit(test_habit)

def test_adding_existing_habit(test_user, test_habit, test_user_from_db, capfd):
    """Tests adding a habit that already exists in the database"""

    # In case test data already exists
    existing = fetch_habit(test_habit.name, test_habit.description, test_habit.periodicity.name, test_user.id)
    if existing:
        delete_habit(existing["id"])

    test_user.id = test_user_from_db["id"]

    # Adds a habit into user's habits list
    test_user.add_habit(test_habit)

    # Adds the same habit again
    test_user.add_habit(test_habit)

    # Capture printed output
    out, err = capfd.readouterr()

    # Checks if the printed message is as expected
    assert "This habit already exists" in out

    # Deletes test habit
    test_user.delete_habit(test_habit)