from flask import Flask
from config import Cfg

app = Flask(__name__)
app.config.from_object(Cfg)

from app import views
