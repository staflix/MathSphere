from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChoiceClassForm(FlaskForm):
    first_class = SubmitField('1 класс')
    second_class = SubmitField('2 класс')
    third_class = SubmitField('3 класс')
    fourth_class = SubmitField('4 класс')
