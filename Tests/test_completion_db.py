import pytest
from datetime import datetime
from enums import Periodicity
from models.habit import Habit
from database_ops.habit_repository import fetch_habit
from database_ops.completion_date_repository import insert_completion_date, fetch_completion_date, delete_completion, fetch_all_completions

@pytest.fixture
def test_habit():
    """This creates a habit object. The habit already exists in the database"""
    habit_from_db = fetch_habit("Change sheets", "Change sheets", Periodicity.WEEKLY.name, "9b5d301d-ec61-402e-9543-d68f86b9c41d")
    habit = Habit(
        name = habit_from_db["name"],
        description = habit_from_db["description"],
        periodicity = Periodicity[habit_from_db["periodicity"]]
        )
    habit.id = habit_from_db["id"]
    return habit

def test_inserting_and_fetching_completion_date(test_habit):
    """Tests if completion is inserted into the database correctly and
    if it is fetched from db"""

    # Inserts completion into the database
    completion_id = insert_completion_date(test_habit, datetime.now())

    # Fetches completion from the database
    completion_date_from_db = fetch_completion_date(completion_id)

    # Checks if fetched completion is not None
    assert completion_date_from_db is not None

    # Deletes inserted completion as it is not needed anymore
    delete_completion(completion_id)

def test_fetching_all_completions(test_habit):
    """Tests fetching all completions for a specific habit"""

    # Inserts 2 completions into the database so there would be what to fetch
    completion_id1 = insert_completion_date(test_habit, datetime.now())
    completion_id2 = insert_completion_date(test_habit, datetime.now())

    # Fetches all completions for the test_habit from the database
    completions_from_db = fetch_all_completions(test_habit.id)

    # Checks if the list of fetched completions is not None and that there are at least 2 completions
    assert completions_from_db is not None
    assert len(completions_from_db) >= 2

    # Deletes inserted completions as they are not needed anymore
    delete_completion(completion_id1)
    delete_completion(completion_id2)

def test_deleting_completion_date(test_habit):
    """Tests deleting completion"""

    # Add a completion so there would be what to delete
    completion_id = insert_completion_date(test_habit, datetime.now())

    # Delete completion from the database
    delete_completion(completion_id)

    # Fetches deleted completion from the database, it should be None
    completion_date_from_db = fetch_completion_date(completion_id)

    # Checks if the fetched completion is None
    assert completion_date_from_db is None