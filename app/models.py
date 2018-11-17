from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app import create_app


class User(UserMixin, db.Model):
    '''
    UserMixin class that includes generic implementations
    that are appropriate for most user model classes
    '''
    __tablename__ = 'users'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(130))
    bio = db.Column(db.String(255))
    profile_pic = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comments', backref='user', lazy="dynamic")
    pitch = db.relationship('Pitch', backref='author', lazy='dynamic')
    likes = db.relationship('Upvote', backref='user', lazy='dynamic')
	dislikes = db.relationship('Downvote', backref='user', lazy='dynamic')



    @property
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
        '''
    with these two methods in place, a user object is now 
    able to do secure password verification
    '''
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    '''
    The new avatar() method of the User class returns the URL of the user's avatar image, 
    scaled to the requested size in pixels.For users that don't have an avatar registered, an "identicon" image will be generated
    The verify_reset_password_token() is a static method, which means that it can be invoked directly from the class
    '''
    def __repr__(self):
        return '{}'.format(self.username)
    '''
    Flask-login modifies the load_userfunction by passing in a user_id to the function that queries the database and gets a User with that ID
    ''' 
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user(cls,id):
        users = User.query.filter_by(User.id=id).all()
        return users

class Pitch(db.Model):
    __tablename__= 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    category = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    likes=db.relationship('Upvote', backref='post', lazy='dynamic')
	dislikes=db.relationship('Downvote', backref='post', lazy='dynamic')
	comments=db.relationship('Comments', backref='post', lazy='dynamic')

    @classmethod
    def retrieve_posts(cls,id):
        pitches = Pitch.filter_by(id=id).all()
        return pitches
    '''
    This class represents the pitches Pitched by 
    users.
    '''
    '''
    The user_id field is initialized as a foreign key to user.id,
    which means that it references an id value from the users table
    '''

    def __repr__(self):
        return '{}'.format(self.body)

        
class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key= True)
    description = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save(self):
		db.session.add(self)
		db.session.commit()

class Upvote(db.Model):
	__tablename__='upvotes'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
	postid=db.Column(db.Integer, db.ForeignKey('pitches.id'))
    '''
    This class defines the likes in each post
    '''
	def save(self):
		db.session.add(self)
		db.session.commit()

class Downvote(db.Model):
	__tablename__='downvotes'
	id=db.Column(db.Integer,primary_key=True)
	userid=db.Column(db.Integer, db.ForeignKey('users.id'))
	postid=db.Column(db.Integer, db.ForeignKey('pitches.id'))
	def save(self):
		db.session.add(self)
		db.session.commit()