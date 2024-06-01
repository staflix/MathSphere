from flask_wtf import FlaskForm
from wtforms import SubmitField


class YandexForm(FlaskForm):
    back = SubmitField('На главную')
