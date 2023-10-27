from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask app configurations
    FLASK_APP = os.environ.get("FLASK_APP")
    FLASK_ENV = os.environ.get("FLASK_ENV")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = os.environ.get("DEBUG") == "True"
