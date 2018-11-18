from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch,Comments,Upvote,Downvote

# Creating app instance
app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)

#Creating the flask shell
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitch=Pitch,Comments=Comments,Upvote=Upvote,Downvote=Downvote )

if __name__ == '__main__':
    manager.run()