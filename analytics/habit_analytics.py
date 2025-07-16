from database_ops.habit_repository import fetch_habits_by_user_id, fetch_habits_by_user_id_and_periodicity
from models.habit import Habit
from enums import Periodicity

def get_active_habits(user):
    """Gets active habits and assigns them to user's list of habits"""

    # Gets user's habits from the database
    db_habits = fetch_habits_by_user_id(user.id)

    # If there are any habits prints their names and descriptions
    if not db_habits:
        return None

    else:
        # For each habit in habits_from_db list, create a habit Object and append it into user's habits list
        for habit_from_db in db_habits:
            # Create a new habit object
            habit = Habit(
                name = habit_from_db["name"],
                description = habit_from_db["description"],
                periodicity = Periodicity[habit_from_db["periodicity"]])
            # Assign habit's id
            habit.id = habit_from_db["id"]

            # Add the habit into the list
            user.habits.append(habit)

def get_same_periodicity_habits(user, periodicity):
    """Gets user's habits with the same periodicity"""

    # Gets habits with the same periodicity
    periodic_habits = fetch_habits_by_user_id_and_periodicity(user.id, periodicity)

    # Checks if there are any habits of the specific periodicity and prints a message
    if not periodic_habits:
        return None

    else:
        # Prints each habit's name and description
        habits_with_same_periodicity = []
        for habit_from_db in periodic_habits:
            habit = Habit(
                name = habit_from_db["name"],
                description = habit_from_db["description"],
                periodicity = Periodicity[habit_from_db["periodicity"]])
            habit.id = habit_from_db["id"]

            habits_with_same_periodicity.append(habit)

        return habits_with_same_periodicity

def get_longest_streak_for_habit(habit):
    """Calculates the longest streak for a specific habit"""

    # Get all completion for the habit
    habit.load_completions()

    # Check if there are any completions for the habit
    if(habit.completion_dates == []):
        return 0

    # Set longest and current streaks
    longest_streak = 0
    current_streak = 1

    # Sort completions from newset to oldest
    sorted_completions = sorted(habit.completion_dates, reverse=True)

    # Iterate through sorted completions to find the longest streak
    for i in range(1, len(sorted_completions)):
        previous_completion = sorted_completions[i - 1]
        current_completion = sorted_completions[i]

        # Calculate streak if habit's periodicity is 'daily' and allow fluctuation of 12 hours
        if habit.periodicity == Periodicity.DAILY:
            # Calculate difference between previous and current completions in hours
            hours_difference = (previous_completion - current_completion).total_seconds() / 3600
            # If the difference is less than 12 hours, it does not count as a streak but does not break the loop either,
            # just continue to the next completion and calculate difference between it and this completion
            if hours_difference < 12:
                continue
            # If the difference is between 12 and 36 hours, it counts as a streak
            elif hours_difference <= 36:
             current_streak += 1
            # If the gap too large, break the loop, assign the longest streak and reset the current streak
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        # Calculate streak if habit's periodicity is 'weekly' and allow fluctuation of 2 days
        elif habit.periodicity == Periodicity.WEEKLY:
            # Calculate days difference between previous (newer) completion and current completion
            days_difference = (previous_completion.date() - current_completion.date()).days

            # If the difference is less than 5 days, it does not count as a streak but does not break the loop either,
            # just continue to the next completion and calculate its difference between it and this completion
            if days_difference < 5:
                continue
            # If the difference is between 5 and 9 days, it counts as a streak
            elif days_difference <= 9:
                current_streak += 1
            # If the gap too large, break the loop, assign the longest streak and reset the current streak
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1

        # Calculate streak if habit's periodicity is 'monthly' and allow fluctuation of 10 days
        elif habit.periodicity == Periodicity.MONTHLY:
            # Calculate days difference between previous (newer) completion and current completion
            days_difference = (previous_completion.date() - current_completion.date()).days

            # If the difference is less than 20 days, it does not count as a streak but does not break the loop either,
            # just continue to the next completion and calculate its difference between it and this completion
            if days_difference < 20:
                continue
            # If the difference is between 20 and 40 days, it counts as a streak
            elif days_difference <=40:
                current_streak += 1
            # If the gap too large, break the loop, assing the longest streak and reset the current streak
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1


    # Final check in case the longest streak is at the end
    longest_streak = max(longest_streak, current_streak)

    return longest_streak

def get_user_longest_streak(user):
    """Gets user's longest streak and a list of habits that the streak belongs 
    to (if there are more than one habit with the same number of streak)"""

    habits_with_longest_streak = []
    longest_streak_of_all_habits = 0

    # For each habit in user's list of habits check if the current habit has a longer streak than the previous one.
    for habit in user.habits:
        # Get current habit's longest streak
        current_habit_longest_streak = get_longest_streak_for_habit(habit)

        # If current habit's longest streak is higher than the streak of all habits,
        # clear the list if habits with longest streak, add current habit into the list and assing 
        # a new longest streak of all habits
        if longest_streak_of_all_habits < current_habit_longest_streak:
            # Empty the list of habits with longest streak
            habits_with_longest_streak.clear()
            # Add current habit into the list of habits with longest streak
            habits_with_longest_streak.append(habit)
            # Assign current habit's longest streak as the longest streak of all habits
            longest_streak_of_all_habits = current_habit_longest_streak

        # If current habit's longest streak is the same as longest streak of all habits,
        # just add the habit into the list of habits with longest streak 
        elif longest_streak_of_all_habits == current_habit_longest_streak:
            habits_with_longest_streak.append(habit)
     
    return (habits_with_longest_streak, longest_streak_of_all_habits)