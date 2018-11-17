import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorna:0724276722@localhost/pitches'

    pass
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}