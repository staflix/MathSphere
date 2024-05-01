from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()], render_kw={"placeholder": "Фамилия"})
    name = StringField('Имя', validators=[DataRequired()], render_kw={"placeholder": "Имя"})
    email = EmailField('Почта', validators=[DataRequired()], render_kw={"placeholder": "Почта"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": "Пароль"})
    password_confirmation = PasswordField('Пароль', validators=[DataRequired()],
                                          render_kw={"placeholder": "Повторите пароль"})
    submit = SubmitField('Зарегистрироваться')
