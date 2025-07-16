# Habit_Tracker

A Python-based habit tracker that allows users to create, manage, and analyze their habits with daily, weekly, or monthly periodicity. Includes analytics like streak tracking and filtering by periodicity.

## Features
Create users and habits
- Mark habits as completed
- Daily, weekly, or monthly periodicity
- Analytics:  
  - Longest streak per habit  
  - Longest streak across all user's habits
  - Filter habits by periodicity  
  - Show active habits
 
## Technologies
- **Python 3.11+**
- **MySQL** (for persistent data)
- **Pytest** (for testing)
- **dotenv** (for environment management)

## Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/EditaGinteryteSidlauskiene/Habit_Tracker.git
   cd Habit_Tracker

2. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Create a .env file
   ```env
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_NAME=habit_tracker

5. Import the Sample Database
To load the pre-populated database:

5.1. Open **MySQL Workbench**.

5.2. Create a new schema named `habit_tracker` if it doesn't already exist:
     ```sql
     CREATE DATABASE habit_tracker;
5.3. Select the habit_tracker schema.

5.4. Click on File → Open SQL Script... and select the provided .sql dump file.
You can find the SQL dump file (`habit_tracker_data.sql`) in the `database/` folder of this repo.

5.5. Click the lightning bolt ⚡️ or press Ctrl + Shift + Enter to run the script.

5.6. The database will now be fully loaded with tables and sample data.

⚠️ Ensure your MySQL Server is running and using a user with privileges to create databases and tables.

## Running Tests
To run tests with pytest:
```bash
pytest
```

## Future Improvements
Add a GUI interface

User registration/login

Secure password storage (e.g., hashing with bcrypt)
