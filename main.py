# This script is used for demonstration and testing purposes only.
# It showcases how the core functionality of the habit tracker works,
# including user login and retrieving analytics like the longest habit streak.
from models.user import User
from database_ops.user_repository import insert_user, fetch_user
from analytics.habit_analytics import get_active_habits, get_same_periodicity_habits, get_longest_streak_for_habit, get_user_longest_streak

def main():
    # Get a user
    user = get_user("Mark", "mark")

    # Get user's habits
    get_active_habits(user)

    # Get user's longest streak and a list of habits that the streak belongs to
    (habits, streak) = get_user_longest_streak(user)

    # Prints information about the longest streak
    print(f"{user.name}'s longest streak is {streak} of habit(s):")

    for habit in habits:
        print(f"{habit.name}")

def create_user(name, email, password):
    """Creates a new user and inserts it into the database"""

    user = User(name, email, password)
    insert_user(user)

def get_user(name, password):
    """Gets user by its name and password from the database and creates a user object"""

    user_from_db = fetch_user(name, password)

    if not user_from_db:
        print("Wrong name and/or password")
        return None

    user = User(
        name = user_from_db["name"],
        email = user_from_db["email"],
        password = user_from_db["password"],
    )

    user.id = user_from_db["id"]
    return user

if __name__ == "__main__":
    main()




