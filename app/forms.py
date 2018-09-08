from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user_name = StringField(label='Username', validators=[DataRequired()])
    user_pswd = PasswordField(label='Password', validators=[DataRequired()])
    keep_logged = BooleanField(label='Remember')
    submit = SubmitField(label='Submit')

