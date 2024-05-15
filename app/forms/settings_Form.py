from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField


class SettingsForm(FlaskForm):
    name = StringField('Имя', render_kw={"placeholder": "Имя"})
    surname = StringField('Фамилия', render_kw={"placeholder": "Фамилия"})
    password = PasswordField('Пароль', render_kw={"placeholder": "Пароль"})
    confirm_password = PasswordField('Повторите пароль', render_kw={"placeholder": "Подтвердите пароль"})
    next = SubmitField("Сохранить изменения")
