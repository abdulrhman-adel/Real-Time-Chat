from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database
from sqlalchemy_utils.functions import database_exists

# Load environment variables from .env file
load_dotenv()


class Config:
    # Flask app configurations
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    # Database configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking and use less memory

    @classmethod
    def validate_database(cls):
        from app import db  # Import db locally to avoid circular import
        engine = create_engine(cls.SQLALCHEMY_DATABASE_URI)
        if not database_exists(engine.url):  # Checks if database exists
            create_database(engine.url)  # If not, create database
            print("New Database Created")
            # Create all the tables if they don't exist
            # TODO: See why this is not working
            db.create_all()
            print("All tables created.")
        else:
            print("Database Already Exists")
