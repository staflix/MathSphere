from flask_wtf import FlaskForm
from wtforms import SubmitField


class ChangeAvatarForm(FlaskForm):
    back = SubmitField('Назад')
    for i in range(1, 61):
        locals()[f"submit{i}"] = SubmitField("Выбрать")
