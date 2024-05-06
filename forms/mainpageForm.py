from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class MainPageForm(FlaskForm):
    register = SubmitField('Зарегистрироваться')
    login = SubmitField('Войти')
