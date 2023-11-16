from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Email


#so we just imported a bunch of tools from flask that verify that the info a user passed in is valid,
#this is so we dont have to write a bunch of regex code.

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()

    #this code above is all imported information structures that have tools to make sure that the user imput has the 
    #requirments to satisfy an email or password.

