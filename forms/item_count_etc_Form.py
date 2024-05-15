from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class ItemCountEtcForm(FlaskForm):
    answer_text = IntegerField('Введите ответ', validators=[DataRequired()])
    check = SubmitField('Проверить')
    next = SubmitField('Дальше')
