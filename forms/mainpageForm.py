from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired


class UnLogMainPageForm(FlaskForm):
    register = SubmitField('Зарегистрироваться')
    login = SubmitField('Войти')


class LogMainPageForm(FlaskForm):
    settings = SubmitField('Настройки')
    change_avatar = SubmitField('Сменить аватар')
    exit = SubmitField('Выйти')
    trainer_btn = SubmitField('Тренажер')
    company_btn = SubmitField('Кампания')
