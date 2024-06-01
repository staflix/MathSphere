from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChoiceTopicClass1Form(FlaskForm):
    topic1 = SubmitField(
        'Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')
    topic2 = SubmitField('Тема2')
    topic3 = SubmitField('Тема3')
    topic4 = SubmitField('Тема4')
    topic5 = SubmitField('Тема5')
    topic6 = SubmitField('Тема6')
    topic7 = SubmitField('Тема7')
    topic8 = SubmitField('Тема8')
