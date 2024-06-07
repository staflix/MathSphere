from flask import render_template, request
import flask
from forms.trainer_class_Form import TrainerClassForm
from generator.generate import *
from data import db_session
from data.users import Info
from flask_login import current_user
from random import choice
from generator.generate import *

blueprint = flask.Blueprint(
    'send_task_for_trainer_api',
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


@blueprint.route('/<int:num_class>/<topic>', methods=['GET', 'POST'])
def send_task_for_trainer(num_class, topic):
    form = TrainerClassForm()
    mix = request.args.get('mix')
    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    if mix:
        topic = random.choice(
            db_sess.query(Info).filter(Info.user_id == current_user.id).first().topics.split("-"))
        for key, value in topics.items():
            if topic in value:
                n_class = key
        task = generate(n_class, topic)
        text = task.task
        answer = task.answer
    else:
        task = generate(num_class, topic)
        text = task.task
        answer = task.answer

    if topic in ['Многоугольники', 'Счет предметов']:
        path_img = task.image[0]
        count_img = len(task.image)
        if str(path_img)[0] not in '1234567890':
            path_img = f'{path_img.split(".")[0]}{count_img}.png'
    else:
        path_img = None
        count_img = 0

    return render_template("task_trainer.html", text=text, answer=answer, path_img=path_img, topic=topic,
                           count_img=count_img, num_class=num_class, form=form,
                           minutes=request.form.get('minutes', 0, type=int),
                           seconds=request.form.get('seconds', 0, type=int),
                           correct_answers=request.form.get('correct_answers', 0, type=int),
                           total_questions=request.form.get('total_questions', 0, type=int),
                           mix=mix)
