from flask import Flask
from app.models import db  
from app.config import Config 

app = Flask(__name__)
app.config.from_object(Config)  
db.init_app(app)  

from app import routes
