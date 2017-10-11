from flask import render_template, redirect, url_for, request, g
from flask_login import login_required, login_user, logout_user, current_user
from app import app, login_manager
from app.models import User, Pomodoro

from app.forms import LoginForm


@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.before_request
def before_request():
    g.user = current_user


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


@app.route('/graph')
@login_required
def graph():
    return render_template('graph.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/pomodoro", methods=["POST"])
@login_required
def pomodoro():
    request_json = request.get_json()
    Pomodoro.create_new_pomodoro(
        request_json['context'],
        request_json['interruptions'],
        g.user.id
    )
    return "", 201
