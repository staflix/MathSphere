from flask import render_template, redirect, request, jsonify, url_for
import flask
from forms.settings_Form import SettingsForm
from data import db_session
from flask_login import current_user
from data.users import User, Info
import random

blueprint = flask.Blueprint(
    'mix_api',
    __name__,
    template_folder='templates'
)

topics = {
    1: ['Счет предметов', 'Многоугольники', 'Задачки на увеличение', 'Задачки на уменьшение', 'Задачки (разнобой)',
        'Примеры на счет'],
    2: ['Числа от 1 до 20', 'Счет десятками', 'Сложение и вычитание (Числа от 1 до 100)', 'Уравнения',
        'Деление и умножение (Начальные)', 'Примеры'],
    3: ['Сложение (Трехзначные числа)', 'Вычитание (Трехзначные числа)', 'Деление (Среднее)', 'Умножение (Среднее)',
        'Деление (Трехзначные числа)', 'Примеры (Трехзначные числа)'],
    4: ['Сложение (Три слагаемых)', 'Сложение (Числа больше 1000)', 'Умножение (На произведение)',
        'Умножение (Продвинутое)', 'Деление (На двузначные)', 'Деление (Продвинутое)']
}


@blueprint.route('/mix', methods=['GET', 'POST'])
def mix():
    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    if request.method == 'POST':
        selected_themes = request.form.getlist('theme')
        topics_f = '-'.join(selected_themes)
        info_user = db_sess.query(Info).filter(Info.user_id == current_user.id).first()
        info_user.topics = topics_f
        db_sess.commit()
        db_sess.close()
        topic = random.choice(topics_f.split('-'))

        for key, value in topics.items():
            if topic in value:
                num_class = key
                break
        return redirect(f'/{num_class}/{topic}?mix=True')
    return render_template("mix.html")
