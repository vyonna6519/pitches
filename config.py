import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS= True
    SECRET_KEY= b'562af35a9b244efba09ef9e1a482d134x9'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:vyonna6519@localhost/one_min_pitch'

     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:vyonna6519@localhost/one_min_pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}