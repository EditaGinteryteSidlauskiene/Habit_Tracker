import pytest
from models.user import User
from database_ops.user_repository import insert_user, fetch_user, delete_user

@pytest.fixture
def test_user():
    """User object is created to test with"""

    return User("TestUser", "test@gmail.com", "pass123")

def test_user_insertion_and_fetching(test_user):
    """Tests user insertion and fetching it from the database"""

    try:
        # Insert user into the database
        insert_user(test_user)

        # Fetches user from the database by its name and password
        user_from_db = fetch_user(test_user.name, test_user.password)

        # Checks if the user was inserted correctly
        assert user_from_db is not None
        assert user_from_db["id"] == test_user.id
        assert user_from_db["name"] == test_user.name
        assert user_from_db["email"] == test_user.email
        assert user_from_db["password"] == test_user.password
    finally:
        # The test user is deleted because it is not needed anymore
        delete_user(test_user.id)

def test_user_deletion(test_user):
    """Tests user deletion"""

    # Inserts test user into the database so there would be what to delete
    insert_user(test_user)

    # Deletes the user from the database
    delete_user(test_user.id)

    # try to get the test user from the database (the result should be None)
    user_from_db = fetch_user(test_user.name, test_user.password)
  
    # Checks if the user was deleted
    assert user_from_db is None
    