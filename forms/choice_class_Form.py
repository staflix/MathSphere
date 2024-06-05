from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChoiceClassForm(FlaskForm):
    first_class = SubmitField('Начать')
    second_class = SubmitField('Начать')
    third_class = SubmitField('Начать')
    fourth_class = SubmitField('Начать')
