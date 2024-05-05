from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, EmailField, HiddenField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()], render_kw={"placeholder": "Почта"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": "Пароль"})
    reset_password = HiddenField('Забыли пароль?')
    input_password = SubmitField('Продолжить')
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
