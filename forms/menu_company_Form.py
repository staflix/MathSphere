from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class MenuCompanyForm(FlaskForm):
    start = SubmitField('Начать')
    close = SubmitField('Закрыть')
    for i in range(1, 401):
        locals()[f"level{i}"] = SubmitField(str(i))
