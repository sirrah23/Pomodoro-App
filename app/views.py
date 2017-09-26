from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, login_user, UserMixin, logout_user
from app import app, login_manager

from .forms import LoginForm

@login_manager.user_loader
def load_user(id):
    return TempUser()

class TempUser(UserMixin):

    id = 1

    def get_id(self):
        return self.id

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        if username:
            # TODO: Add username and password checks
            login_user(TempUser(), False)
            return redirect(request.args.get('next') or url_for('index'))
    flash("Try again")
    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
