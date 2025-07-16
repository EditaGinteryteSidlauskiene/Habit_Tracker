
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Establishes and returns a connection to the MySQL 'habit_tracker' database."""

    return pymysql.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "habit_tracker"),
        port=int(os.getenv("DB_PORT", 3306)),
        cursorclass=pymysql.cursors.DictCursor
        )