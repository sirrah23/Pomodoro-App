from flask_script import Manager, Server, prompt_bool
from app import app, db
from app.models import User

manager = Manager(app)
manager.add_command("runserver", Server())

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="admin", password="admin"))
    db.session.commit()

@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to delete the database?"):
        db.drop_all()
        print("Dropped the database")

if __name__ == "__main__":
    manager.run()
