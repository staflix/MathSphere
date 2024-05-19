from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class CompanyLevelForm(FlaskForm):
    answer1 = SubmitField('Проверить')
    answer2 = SubmitField('Проверить')
    answer3 = SubmitField('Проверить')
    answer4 = SubmitField('Проверить')
    text_answer = IntegerField("Введите ответ")
    check_answer = SubmitField("Ответить")
    right = SubmitField('Дальше')
    left = SubmitField('Назад')
    leave = SubmitField('Вернуться')
