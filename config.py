import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:0724276722@localhost/pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    pass
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}