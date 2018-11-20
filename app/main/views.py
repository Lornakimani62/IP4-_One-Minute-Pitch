from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import Pitch,Comment,User,Like,Dislike
from .forms import UpdateProfile,PitchForm,CommentForm


#landing page
@main.route('/')
def index():
    title = 'Dashboard' if current_user.is_authenticated else 'Home'
    posts = Pitch.query.all()
    return render_template('index.html')

# This view function defines the profile of the user
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

# This view function defines the update profile functionality

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# This view function defines upload photo functionality

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

# This view function allows uses to post new pitches

@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()

    interviewpitches = Pitch.query.filter_by(category="Interview-Pitch").all()
    productpitches = Pitch.query.filter_by(category="Product-Pitch").all()
    promotionpitches = Pitch.query.filter_by(category="Promotion-Pitch").all()
    businesspitches = Pitch.query.filter_by(category="Business-Pitch").all()

    pitches = Pitch.query.filter().all()
    likes = Like.get_all_likes(pitch_id=Pitch.id)
    dislikes = Dislike.get_all_dislikes(pitch_id=Pitch.id)

    if pitch_form.validate_on_submit():

        pitch_title= pitch_form.pitch_title.data
        content= pitch_form.content.data
        category=pitch_form.category.data

        # Updated  instance
        new_pitch = Pitch(pitch_title=pitch_title,content=content,category=category,user=current_user)
        pitches = Pitch.query.filter().all()
        # save  method
        new_pitch.save_pitch()

        return redirect(url_for('main.new_pitch'))

    title = 'New Pitch'
    return render_template('new_pitch.html',title = title, pitch_form=pitch_form, interviewpitches = interviewpitches, productpitches = productpitches, promotionpitches = promotionpitches, businesspitches = businesspitches, likes=likes, dislikes=dislikes)

#Returns all the user's posts on the profile page
@main.route('/pitch/<int:id>', methods = ['GET','POST'])
@login_required
def user_post(id):

    users_post = Pitch.query.filter_by(user_id=id)
    return render_template('profile/profile.html',users_post = users_post)

# This function allows users to comment on pitches
@main.route('/comment/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    comment = Comment.query.filter_by(pitch_id=id)

    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        comment_content = form_comment.details.data

        new_comment = Comment(comment_content= comment_content,pitch_id=id,user=current_user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('comments.html',form_comment = form_comment,comment=comment)

#Returns likes on the pitch
@main.route('/like/<int:id>')
def like(id):
    if current_user.is_authenticated:
        if current_user.likes.filter_by(Upvote.pitch_id==id).first():
            return 'Error'
        Upvote(userid=current_user.id,pitch_id=id).save()
        return 'Success'
    return 'Error'

#Returns dislike on the pitch
@main.route('/dislike/<int:id>')
def dislike(id):
    if current_user.is_authenticated:
        if current_user.dislikes.filter(Downvote.postid==id).first():
            return 'Error'
        Downvote(userid=current_user.id,postid=id).save()
        return 'Success'
    return 'Error'