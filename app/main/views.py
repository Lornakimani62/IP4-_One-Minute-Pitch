from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from .. import db
from ..models import Pitch,Comment,User,Like,Dislike

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    interviewpitches = Pitch.query.filter_by(category="Interview-Pitch").all()
    productpitches = Pitch.query.filter_by(category="Product-Pitch").all()
    promotionpitches = Pitch.query.filter_by(category="Promotion-Pitch").all()
    businesspitches = Pitch.query.filter_by(category="Business-Pitch").all()

    pitches = Pitch.query.filter_by().first()
    likes = Like.get_all_likes(pitch_id=Pitch.id)
    dislikes = Dislike.get_all_dislikes(pitch_id=Pitch.id)

    return render_template('post.html', interviewpitches = interviewpitches, productpitches = productpitches, promotionpitches = promotionpitches, businesspitches = businesspitches, likes=likes, dislikes=dislikes)