from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class CompanyLevelForm(FlaskForm):
    answer1 = SubmitField('Проверить')
    answer2 = SubmitField('Проверить')
    answer3 = SubmitField('Проверить')
    answer4 = SubmitField('Проверить')
    text_answer = IntegerField("Введите ответ", validators=[DataRequired()])
    finish = SubmitField('Закончить')
    check_answer = SubmitField("Ответить")
    next = SubmitField('Дальше')
    prev = SubmitField('Назад')

