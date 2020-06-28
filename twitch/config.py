import os
config_path=os.path.abspath(os.path.dirname(__file__))#當前目錄
class Config:
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:a123456@localhost:3306/twitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='abc123'
    TWEET_PER_PAGE=3

    # MAIL_DEFAULT_SENDER ='noreply@twittor.com'
    # MAIL_SERVER =  'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS =  1
    # MAIL_USERNAME = 'testshih0524@gmail.com'
    # MAIL_PASSWORD = 'flask0524'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@twittor.com')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 1)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'testshih0524@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'flask0524')
    MAIL_SUBJECT_RESET_PASSWORD = '[Twitch] Please Reset Your Password'
    MAIN_SUBJECT_USER_ACTIVATE = '[Twitch] Please Activate Your Accout'
