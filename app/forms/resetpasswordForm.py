from flask_wtf import FlaskForm
from wtforms import SubmitField


class ResetPasswordForm(FlaskForm):
    submit = SubmitField('Подтвердить')
    back = SubmitField('Вернуться')
