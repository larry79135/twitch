from flask_script import Manager
from flask_migrate import MigrateCommand
from twitch import create_app



app=create_app()
manager=Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    print("hello")

if __name__ == "__main__":
    manager.run()