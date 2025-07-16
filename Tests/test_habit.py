import pytest
from datetime import datetime, date
from models.habit import Habit
from enums import Periodicity
from database_ops.habit_repository import fetch_habit
from database_ops.completion_date_repository import fetch_all_completions, delete_completion

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

def test_habit_creation():
    """Tests if a habit is created correctly"""

    habit = Habit("Jogging", "Jog for 30 min", Periodicity.DAILY)

    assert habit.name == "Jogging"
    assert habit.description == "Jog for 30 min"
    assert habit.periodicity == Periodicity.DAILY
    assert habit.completion_dates == []
    assert isinstance(habit.creation_date, datetime)

def test_habit_creation_fails_without_name():
    """Tests if the correct error is thrown when a habit is being created without a name"""

    with pytest.raises(ValueError, match="Habit's name cannot be empty."):
        Habit("", "Jog for 30 min", Periodicity.DAILY)

def test_habit_creation_fails_without_description():
    """Tests if the correct error is thrown when a habit is being created without a description"""

    with pytest.raises(ValueError, match="Habit's description cannot be empty."):
        Habit("Jogging", "", Periodicity.DAILY)

def test_habit_creation_fails_without_periodicity():
    """Tests if the correct error is thrown when a habit is being created without a periodicity"""

    with pytest.raises(ValueError, match="Habit's periodicity cannot be empty or other than daily, weekly, monthly."):
        Habit("Jogging", "Jog for 30 min", 1)

def test_habit_ids_are_unique():
    """Tests if habits' ids are unique"""

    habit1 = Habit("Drink water", "8 glasses a day", Periodicity.DAILY)
    habit2 = Habit("Eat vegetables", "7 units a day", Periodicity.DAILY)
    assert habit1.id != habit2.id

def test_marking_as_completed(test_habit):
    """Tests if completion date is added into the list completion_dates successfully"""

    # A new completion date is added to the list of completion_dates for test habit and completion id id returned
    completion_id = test_habit.mark_as_completed()

    # Check if the list of completion_dates is not empty and if today's date is in the list
    assert test_habit.completion_dates != []
    assert any(completion_date.date() == date.today() for completion_date in test_habit.completion_dates)

    # Gets completion date from the database
    completions = fetch_all_completions(test_habit.id)

    # Checks if today's completion is in the list of completions
    assert any(
    completion['completed_on'].date() == date.today()
    for completion in completions
    )

    # Delete completion from habit object and the database
    test_habit.completion_dates.pop()
    delete_completion(completion_id)

def test_laoding_completions(test_habit):
    """Tests getting completions from the database and adding them into the list of habit's completion dates"""

    # Gets completions
    test_habit.load_completions()

    # Checks if the list of habit's completion dates is not empty
    assert test_habit.completion_dates != []