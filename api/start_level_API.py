from flask import render_template, request, redirect
import flask
from forms.company_levelForm import CompanyLevelForm
from data import db_session
from data.users import User, Info
from company.company_second_class import *

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

    if request.method == 'POST' and form.validate_on_submit():
        if form.finish.data:
            if str(user.profile_level) <= level:
                user.profile_level = int(level) + 1
                db_sess.commit()
            db_sess.close()
            return redirect(f'/menu_company/key={rdm_string}')

    if 101 <= int(level) <= 200:
        timer, topic, tasks, answers, choices, imgs = get_level_data(year_2, level)
        return render_template("level.html", timer=timer, choice=choices, img=imgs,
                               topic=topic, tasks=tasks, rdm_string=rdm_string, answers=answers, form=form)


def get_level_data(year, level_selected):
    topic_index = (int(level_selected) // 10) % 10
    level_within_topic_index = (int(level_selected) - 1) % 10
    timer = None
    if int(level_selected) % 10 == 0 and int(level_selected) % 100 != 0:
        timer = "10:00"
        topic_index -= 1
    elif int(level_selected) % 10 == 0 and int(level_selected) % 100 == 0:
        timer = "20:00"
        topic_index = 9

    selected_topic = year.topics[topic_index]
    selected_level = selected_topic.levels[level_within_topic_index]

    topic = selected_topic.name
    tasks = [task.task for task in selected_level.tasks]
    answers = [task.answer for task in selected_level.tasks]
    choices = [task.choice if task.choice else None for task in selected_level.tasks]
    imgs = [task.image if task.image else None for task in selected_level.tasks]

    return timer, topic, tasks, answers, choices, imgs
