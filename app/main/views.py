from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import Pitch,Comments,User,Upvote,Downvote

# @main.route('/index', methods=['GET', 'POST'])
# def home():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Pitch(body=form.post.data, author=current_user, category=form.category.data)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post is now live!')
#         return redirect(url_for('main.index'))

#     posts = Pitch.retrieve_posts(id).all()

#     return render_template("posts.html", title='Home Page', form=form,posts=posts)