from flask import Flask
from app.models import db  # Import the db object from models
from app.config import Config  # Import Config from config

app = Flask(__name__)
app.config.from_object(Config)  # Use the imported Config class
db.init_app(app)  # Initialize the db with the Flask app

from app import routes
