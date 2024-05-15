from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class MenuCompanyForm(FlaskForm):
    answer_text = StringField('Введите ответ', validators=[DataRequired()])
    check = SubmitField('Проверить')
    next = SubmitField('Дальше')
