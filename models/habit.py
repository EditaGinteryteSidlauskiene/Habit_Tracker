
import uuid
from datetime import datetime
from enums import Periodicity
from database_ops.completion_date_repository import insert_completion_date, fetch_all_completions

def check_habit_inputs(name, description, periodicity):
    """Checks habits inputs. They must not be empty"""

    if not name:
        raise ValueError("Habit's name cannot be empty.")
    if not description:
       raise ValueError("Habit's description cannot be empty.")
    if periodicity not in (Periodicity.DAILY, Periodicity.WEEKLY, Periodicity.MONTHLY):
       raise ValueError("Habit's periodicity cannot be empty or other than daily, weekly, monthly.")

class Habit:
    """Represents a user habit with tracking for completion and periodicity."""

    def __init__(self, name, description, periodicity):
        check_habit_inputs(name, description, periodicity)

        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.completion_dates = []
        self.creation_date = datetime.now()

    def mark_as_completed(self):
        """Adds completion date"""

        completed_on = datetime.now()

        # Adds completion date to the list of completion_dates
        self.completion_dates.append(completed_on)

        # Inserts completion into the database and returns its id
        completion_id = insert_completion_date(self, completed_on)

        return completion_id

    def load_completions(self):
        """Gets completions from the database and adds them into habit's list of completions"""

        # Get completions from the database
        completions = fetch_all_completions(self.id)

        self.completion_dates.clear()
        # Add each completion into the list
        for completion in completions:
            self.completion_dates.append(completion["completed_on"])