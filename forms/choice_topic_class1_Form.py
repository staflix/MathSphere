from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChoiceTopicClass1Form(FlaskForm):
    item_count_etc = SubmitField(
        'Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')
    topic1 = SubmitField('.!.')
    topic2 = SubmitField('.!.')
    topic3 = SubmitField('.!.')
