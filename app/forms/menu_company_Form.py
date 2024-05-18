from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class MenuCompanyForm(FlaskForm):
    start = SubmitField('Начать')
    close = SubmitField('Закрыть')
    level1 = SubmitField("1")
    level2 = SubmitField("2")