from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, UserMixin, logout_user
from app import app, login_manager
from app.models import User

from app.forms import LoginForm

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        print(user)
        if user is not None and user.check_password(form.password.data):
            login_user(user, False)
            return redirect(request.args.get('next') or url_for('index'))
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
