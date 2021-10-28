from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Cfg

app = Flask(__name__)
app.config.from_object(Cfg)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models
