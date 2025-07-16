import pytest
from database_ops.user_repository import fetch_user
from enums import Periodicity
from models.user import User
from models.habit import Habit
from analytics.habit_analytics import get_active_habits, get_same_periodicity_habits, get_longest_streak_for_habit, get_user_longest_streak
from database_ops.habit_repository import fetch_habit, fetch_habits_by_user_id

@pytest.fixture
def user_from_db():
    """Gets an existing user from the database to be used for testing"""

    # Gets user from db
    user_from_db = fetch_user("William", "william")

    # Create a user object with user's from db data
    user = User(
        name = user_from_db["name"],
        email = user_from_db["email"],
        password = user_from_db["password"])

    # Assign users' from db id to the user object
    user.id = user_from_db["id"]
    return user

@pytest.fixture
def user_with_no_habits_from_db():
    """Gets an existing user who has no habits from the database"""

    # Gets user from db
    user_from_db = fetch_user("Oliver", "oliver")

    # Create a user object with user's from db data
    user = User(
        name = user_from_db["name"],
        email = user_from_db["email"],
        password = user_from_db["password"])

    # Assign users' from db id to the user object
    user.id = user_from_db["id"]
    return user

@pytest.fixture
def test_habit_with_daily_periodicity():
    """This creates a habit object whose periodicity is 'daily'. The habit already exists in the database"""

    habit_from_db = fetch_habit("Jogging", "Jog for 30 min", Periodicity.DAILY.name, "3bbe0fe5-5964-4c0f-aee3-fe85057c9877")
    habit = Habit(
        name = habit_from_db["name"],
        description = habit_from_db["description"],
        periodicity = Periodicity[habit_from_db["periodicity"]]
        )
    habit.id = habit_from_db["id"]
    return habit

@pytest.fixture
def test_habit_with_daily_periodicity_and_zero_completions():
    """This creates a habit object whose periodicity is 'daily' but does not have any completions. 
    The habit already exists in the database"""

    habit_from_db = fetch_habit("Brush teeth", "twice a day", Periodicity.DAILY.name, "b6b47614-afcb-454e-9a3a-a9f815e91568")
    habit = Habit(
        name = habit_from_db["name"],
        description = habit_from_db["description"],
        periodicity = Periodicity[habit_from_db["periodicity"]]
        )
    habit.id = habit_from_db["id"]
    return habit

@pytest.fixture
def test_habit_with_weekly_periodicity():
    """This creates a habit object whose periodicity is 'weekly'. The habit already exists in the database"""
    habit_from_db = fetch_habit("Laundry", "Do laundry", Periodicity.WEEKLY.name, "b6b47614-afcb-454e-9a3a-a9f815e91568")
    habit = Habit(
        name = habit_from_db["name"],
        description = habit_from_db["description"],
        periodicity = Periodicity[habit_from_db["periodicity"]]
        )
    habit.id = habit_from_db["id"]
    return habit

@pytest.fixture
def test_habit_with_weekly_periodicity_and_zero_completions():
    """This creates a habit object whose periodicity is 'weekly' but does not have any completions.
    The habit already exists in the database"""
    habit_from_db = fetch_habit("Grass", "Mowe grass", Periodicity.WEEKLY.name, "d0697617-54c3-4237-9ad2-ddc93ef02079")
    habit = Habit(
        name = habit_from_db["name"],
        description = habit_from_db["description"],
        periodicity = Periodicity[habit_from_db["periodicity"]]
        )
    habit.id = habit_from_db["id"]
    return habit

@pytest.fixture
def test_habit_with_monthly_periodicity():
    """This creates a habit object whose periodicity is 'monthly'. The habit already exists in the database"""

    habit_from_db = fetch_habit("Trash container", "Take out trash container", Periodicity.MONTHLY.name, "d0697617-54c3-4237-9ad2-ddc93ef02079")
    habit = Habit(
        name = habit_from_db["name"],
        description = habit_from_db["description"],
        periodicity = Periodicity[habit_from_db["periodicity"]]
        )
    habit.id = habit_from_db["id"]
    return habit

@pytest.fixture
def test_habit_with_monthly_periodicity_and_zero_completions():
    """This creates a habit object whose periodicity is 'monthly' but does not have any completions.
    The habit already exists in the database"""

    habit_from_db = fetch_habit("Bills", "Pay bills", Periodicity.MONTHLY.name, "9b5d301d-ec61-402e-9543-d68f86b9c41d")
    habit = Habit(
        name = habit_from_db["name"],
        description = habit_from_db["description"],
        periodicity = Periodicity[habit_from_db["periodicity"]]
        )
    habit.id = habit_from_db["id"]
    return habit

def test_getting_active_habits(user_from_db):
    """Tests getting active habits and printing out their names and descriptions"""

    # Gets active habits and prints them out
    get_active_habits(user_from_db)

    # Collect habit names from the user's habits
    habit_names = [habit.name for habit in user_from_db.habits]

    # Checks if the exactly 2 habits are fetched and one habit's name is 'Jogging' and the other's 'Drink water'
    assert user_from_db.habits != []
    assert len(user_from_db.habits) == 2
    assert "Jogging" in habit_names
    assert "Drink water" in habit_names

def test_getting_active_habits_for_user_with_no_habits(user_with_no_habits_from_db):
    """Tests getting active habits for the user, who does not have any habits"""

    # Gets active habits and prints them out
    get_active_habits(user_with_no_habits_from_db)

    # Checks if there are no habits if user's list
    assert user_with_no_habits_from_db.habits == []

def test_getting_same_periodicity_habits(user_from_db):
    """Tests getting user's habits with the same periodicity"""

    habits_with_same_periodicity = get_same_periodicity_habits(user_from_db, Periodicity.DAILY)

    # Collect habit names from the user's habits
    habit_periodicities = [habit.periodicity for habit in habits_with_same_periodicity]

    # Checks if the list of habits is not empty, and there are exactly 2 habits if the same periodicity, which 'Daily'
    assert habits_with_same_periodicity != None
    assert habits_with_same_periodicity != []
    assert len(habits_with_same_periodicity) == 2
    assert Periodicity.DAILY in habit_periodicities
    assert Periodicity.WEEKLY not in habit_periodicities
    assert Periodicity.MONTHLY not in habit_periodicities

def test_getting_same_periodicity_habits_with_periodicity_user_does_not_have(user_from_db, capsys):
    """Tests getting user's habits with same periodicity when there are no habits with such periodicity"""

    periodicity = Periodicity.WEEKLY

    # Gets habits with same periodicity, it should not get anything
    habits_with_same_periodicity = get_same_periodicity_habits(user_from_db, periodicity)

    # Checks if the list of habits with the same periodicity in None
    assert habits_with_same_periodicity == None

def test_getting_longest_streak_for_habit_with_daily_periodicity(test_habit_with_daily_periodicity):
    """Tests calculating the longest streak for a habit with daily periodicity"""

    # Get the longest streak for the habit
    longest_streak = get_longest_streak_for_habit(test_habit_with_daily_periodicity)

    # Check if calculated streak is exactly what was expected
    assert longest_streak == 6

def test_getting_longest_streak_for_habit_with_daily_periodicity_and_zero_completions(
    test_habit_with_daily_periodicity_and_zero_completions):
    """Tests calculating the longest streak for a habit with daily periodicity and that does not have any completions"""

    # Get the longest streak for the habit
    longest_streak = get_longest_streak_for_habit(
        test_habit_with_daily_periodicity_and_zero_completions)

    # Check if calculated streak is exactly what was expected
    assert longest_streak == 0

def test_getting_longest_streak_for_habit_with_weekly_periodicity(test_habit_with_weekly_periodicity):
    """Tests calculating the longest streak for a habit with weekly periodicity"""

    # Get the longest streak for the habit
    longest_streak = get_longest_streak_for_habit(test_habit_with_weekly_periodicity)

    # Check if calculated streak is exactly what was expected
    assert longest_streak == 4

def test_getting_longest_streak_for_habit_with_weekly_periodicity_and_zero_completions(
    test_habit_with_weekly_periodicity_and_zero_completions):
    """Tests calculating the longest streak for a habit with weekly periodicity and that does not have any completions"""

    # Get the longest streak for the habit
    longest_streak = get_longest_streak_for_habit(
        test_habit_with_weekly_periodicity_and_zero_completions)

    # Check if calculated streak is exactly what was expected
    assert longest_streak == 0

def test_getting_longest_streak_for_habit_with_monthly_periodicity(test_habit_with_monthly_periodicity):
    """Tests calculating the longest streak for a habit with monthly periodicity"""

    # Get the longest streak for the habit
    longest_streak = get_longest_streak_for_habit(test_habit_with_monthly_periodicity)

    # Check if calculated streak is exactly what was expected
    assert longest_streak == 3

def test_getting_longest_streak_for_habit_with_monthly_periodicity_and_zero_completions(
    test_habit_with_monthly_periodicity_and_zero_completions):
    """Tests calculating the longest streak for a habit with monthly periodicity and that does not have any completions"""

    # Get the longest streak for the habit
    longest_streak = get_longest_streak_for_habit(
        test_habit_with_monthly_periodicity_and_zero_completions)

    # Check if calculated streak is exactly what was expected
    assert longest_streak == 0

def test_getting_user_longest_streak(user_from_db):
    """Tests getting longest streak of all user's habits"""

    # Get user's habits from the database
    user_habits = fetch_habits_by_user_id(user_from_db.id)

    # Add each habit from db into user's list of habits
    for habit_from_db in user_habits:

        habit = Habit(
            name = habit_from_db["name"],
            description = habit_from_db["description"],
            periodicity = Periodicity[habit_from_db["periodicity"]])

        habit.id = habit_from_db["id"]
        user_from_db.habits.append(habit)

    # Get a list of habits that have the same longest streak and the streak itself
    (habits, streak) = get_user_longest_streak(user_from_db)

    # Check habits is a list, and streak is integer
    assert isinstance (habits, list)
    assert isinstance (streak, int)

    # Check if streak, number of habits with the longest streak, and habit's name are as expected
    assert streak == 6
    assert len(habits) == 1
    assert habits[0].name == "Jogging"

