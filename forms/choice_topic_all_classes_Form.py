from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChoiceTopicAllClassesForm(FlaskForm):
    topic11 = SubmitField(
        'Счет предметов. Сравнение групп предметов. Пространственные и временные представления.')
    topic12 = SubmitField('Многоугольники')
    topic13 = SubmitField('Задачки на увеличение')
    topic14 = SubmitField('Задачки на уменьшение')
    topic15 = SubmitField('Задачки (разнобой)')
    topic16 = SubmitField('Примеры на счет')
    topic17 = SubmitField('Тима тома ни разлий вода!+!+_"_"')
    topic18 = SubmitField('BANKAII КАНУМБИРАЧИ ИНЫШМЕ АРАТЕМУ ТУДУДУДУ ТУДУДУДУ')
