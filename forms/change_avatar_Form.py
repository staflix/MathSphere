from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChangeAvatarForm(FlaskForm):
    back = SubmitField('Назад')
    submit1 = SubmitField('Выбрать')
    submit2 = SubmitField('Выбрать')
    submit3 = SubmitField('Выбрать')
    submit4 = SubmitField('Выбрать')
    submit5 = SubmitField('Выбрать')
    submit6 = SubmitField('Выбрать')
    submit7 = SubmitField('Выбрать')
