from flask_script import Manager, Server, prompt_bool, prompt, prompt_pass
from project.app import app, db
from project.app.models import User

manager = Manager(app)
manager.add_command("runserver", Server())


@manager.command
def initdb():
    db.create_all()


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to delete the database?"):
        db.drop_all()
        print("Dropped the database")


@manager.command
def adduser():
    username = prompt("Username?")
    password = prompt_pass("Password?")
    db.session.add(User(username=username, password=password))
    db.session.commit()
    print("Created the new user: " + username)


if __name__ == "__main__":
    manager.run()
