from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import Pitch,Comment,User,Like,Dislike
from .forms import UpdateProfile,PitchForm,CommentForm

#This view function defines categories

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    interviewpitches = Pitch.query.filter_by(category="Interview-Pitch").all()
    productpitches = Pitch.query.filter_by(category="Product-Pitch").all()
    promotionpitches = Pitch.query.filter_by(category="Promotion-Pitch").all()
    businesspitches = Pitch.query.filter_by(category="Business-Pitch").all()

    pitches = Pitch.query.filter().all()
    likes = Like.get_all_likes(pitch_id=Pitch.id)
    dislikes = Dislike.get_all_dislikes(pitch_id=Pitch.id)

    return render_template('index.html', interviewpitches = interviewpitches, productpitches = productpitches, promotionpitches = promotionpitches, businesspitches = businesspitches, likes=likes, dislikes=dislikes)

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
