from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

#to be used with html form of email, password and submit to generate new account
class UserLoginForm(FlaskForm):
    #first_name and last_name do not have the DataRequired() validator, letting them stay blank if user prefers
    # since there are placeholders for it to be a blank string in database
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit_button = SubmitField()