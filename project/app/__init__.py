import os
from flask import Flask, render_template
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from project.app.config import BaseConfig

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.init_app(app)

from . import views
