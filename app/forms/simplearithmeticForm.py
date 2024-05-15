from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SimpleArithmeticForm(FlaskForm):
    answer = StringField('Ответить', validators=[DataRequired()])
    check = SubmitField('Проверить')
    next = SubmitField('Продолжить')
