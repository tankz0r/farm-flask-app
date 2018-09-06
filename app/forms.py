from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(object):
    user_name = StringField(label='username', validators=DataRequired())
    user_pswd = PasswordField(label='pswd', validators=DataRequired())
    keep_logged = BooleanField(label='remember me')
    submit = SubmitField(label='submit')

