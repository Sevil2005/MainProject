from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(Form):
    email = StringField('E-mail', validators = [InputRequired()])
    password = PasswordField('Parol', validators = [InputRequired()])

class RegisterForm(Form):
    name = StringField('Ad', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired()])
    password = PasswordField('Parol', validators=[InputRequired()])
