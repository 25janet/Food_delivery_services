import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_database_url():
    return os.getenv("DATABASE_URL",
                     "postgresql://food_user:food_password@localhost:5432/user_db")