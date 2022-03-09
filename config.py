import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS= False
    # SECRET_KEY= '562af35a9b244efba09ef9e1a482d134x9'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    DATABASE_URL="postgresql://klsunfjvzymaje:e1cbc0b16cc1c7220244939f14054179bdbeb62fbaf906ce8aa1a4e5e0a3c933@ec2-52-45-83-163.compute-1.amazonaws.com:5432/dh90kbtvo3kid"
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:vyonna6519@localhost/one_min_pitch'

     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass 

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # pass
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
       SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    pass 

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:vyonna6519@localhost/one_min_pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}