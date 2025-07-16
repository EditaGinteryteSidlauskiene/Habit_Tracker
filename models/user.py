import uuid
from email_validator import validate_email, EmailNotValidError
from models.habit import Habit
from database_ops.habit_repository import fetch_habits_by_user_id, delete_habit, insert_habit

def check_user_inputs(name, email, password):
    """Checks if user inputs are valid: they must not be empty and email must be valid"""

    if not name:
        raise ValueError("Name cannot be empty.")
    if not email:
        raise ValueError("Email cannot be empty.")
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValueError("Email is not valid.")
    if not password:
        raise ValueError("Password cannot be empty.")

class User:
    """Represents a user with adding and deleting habits from habits list."""

    def __init__(self, name, email, password):
        check_user_inputs(name, email, password)

        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = password
        self.habits = []

    def add_habit(self, habit: Habit):
        """Adds a habit into user's habits list and database"""

        # Gets all habits that belong to the user
        user_habits_from_db = fetch_habits_by_user_id(self.id)

        if user_habits_from_db is not None:

            # Checks if the user already has the same habit
            for habit_in_list in user_habits_from_db:
                if (
                    habit_in_list["name"] == habit.name and
                    habit_in_list["description"] == habit.description and
                    habit_in_list["periodicity"] == habit.periodicity.name and
                    habit_in_list["user_id"] == self.id
                    ):
                    print("This habit already exists")
                    return None
        
        # Adds the habit into user's habits list
        self.habits.append(habit)

        # Inserts the habit into database
        insert_habit(habit, self.id)

    def delete_habit(self, habit: Habit):
        """Deletes habit from user's habits list and database"""

        # Checks if there is a habit in user's habits list
        if (habit in self.habits):
            # Removes the habit
            self.habits.remove(habit)

        # Deletes habit from the database 
        delete_habit(habit.id)  
    