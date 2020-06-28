from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
from twitch.models.user import User

class LoginForm(FlaskForm):
    class Meta:
        csrf= False
    username= StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    remeber_me=BooleanField("Remeber Me")
    submit=SubmitField("Sign In")


class RegisterForm(FlaskForm):
    username= StringField("Username",validators=[DataRequired()])
    email= StringField("Email Address",validators=[DataRequired(), Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    password2=PasswordField("Password Repeat",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')

    def validate_username(self,username):#查看是否有重複
        user=User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use different name')
    def validate_email(self,email):#查看是否有重複
        user=User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use different email address')


class EditProfileForm(FlaskForm):
    about_me =TextAreaField('About me',validators=[Length(min=0,max=120)])
    submit=SubmitField('Save')


class Tweetform(FlaskForm):
    tweet =TextAreaField('Tweet',validators=[DataRequired(), Length(min=0, max=140)])
    submit=SubmitField('Tweet')

class PasswdResetRequestForm(FlaskForm):
    email=StringField("Email Address", validators=[DataRequired(), Email()])
    submit= SubmitField('Reset Password')

    def validate_email(self, email):#查找email
        user=User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('You do not have an account for this email address')

class PasswdResetForm(FlaskForm):
    password=PasswordField("Password",validators=[DataRequired()])
    password2=PasswordField("Password Reset",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Submit')