from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twitch.config import Config
from flask_login import LoginManager
from flask_mail import Mail

db= SQLAlchemy()
migrate=Migrate()
login_manager = LoginManager()
login_manager.login_view ='login'
mail=Mail()
from twitch.route import index,login ,logout,register,user,page_not_found,edit_profile,reset_password_request,\
    password_reset,explore, user_activate

def create_app():
    app=Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:a123456@localhost:3306/twitch'
    # #app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///twitch.db"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config.from_object(Config)
    db.init_app(app)#初始化app
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    app.add_url_rule('/index','index',methods=['GET', 'POST'])
    app.add_url_rule('/','index',index,methods=['GET','POST'])
    app.add_url_rule('/login','login',login,methods=['GET','POST'])
    app.add_url_rule('/logout','logout',logout)
    app.add_url_rule('/register','register',register,methods=['GET','POST'])
    app.add_url_rule('/<username>','profile',user,methods=['GET','POST'])
    app.add_url_rule('/edit_profile','edit_profile',edit_profile,methods=['GET','POST'])
    app.add_url_rule('/reset_password_request','reset_password_request',reset_password_request,methods=['GET', 'POST'])
    app.add_url_rule(
        '/password_reset/<token>',
        'password_reset',
        password_reset,
        methods=['GET', 'POST']
    )
    app.register_error_handler(404,page_not_found)
    app.add_url_rule('/explore','explore',explore)
    app.add_url_rule('/activate/<token>', 'user_activate', user_activate)
    return app

