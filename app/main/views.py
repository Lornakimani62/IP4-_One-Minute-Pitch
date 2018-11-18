from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import Pitch,Comments,User,Upvote,Downvote

@main.route('/')
def home():
    posts = Pitch.query.all()
    categories = db.session.query(Pitch.category).distinct().all()
    defaultcategories = [('pickup lines',),('interview pitch',),('product pitch',),('business pitch',)]
    categories = set(categories+defaultcategories)
    print(categories)
    return render_template('post.html', title = title,posts=posts,categories=categories)