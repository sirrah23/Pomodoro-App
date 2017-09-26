from flask import Flask, render_template
from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'login'
login_manager.init_app(app)

from . import views
