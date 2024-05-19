from flask import render_template, request, redirect
import flask
from app.forms.company_levelForm import CompanyLevelForm
from app.data import db_session
from app.data.users import User, Info
from app.company.company_second_class import *

blueprint = flask.Blueprint(
    'start_level_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/start_level/<level>/key=<rdm_string>', methods=['GET', 'POST'])
def start_level(level, rdm_string):
    form = CompanyLevelForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()

    db_sess.close()

    if request.method == 'POST' and form.validate_on_submit():
        if form.leave.data:
            return redirect(f'/menu_company/key={rdm_string}')

    if level == "1":
        timer = None
        return render_template("level.html", timer=timer, form=form)

    elif level == "101":
        topic = year_2.topics[0].name
        task = year_2.topics[0].levels[0].tasks
        task1 = task[0].task
        task1_answer = task[0].answer
        task2 = task[1].task
        task2_answer = task[1].answer
        task3 = task[2].task
        task3_answer = task[2].answer
        task4 = task[3].task
        task4_answer = task[3].answer
        tasks = [task1, task2, task3, task4]
        answers = [task1_answer, task2_answer, task3_answer, task4_answer]

        return render_template("level.html", timer=None, choice=None, img=None, topic=topic, tasks=tasks,
                               rdm_string=rdm_string, answers=answers, form=form)
