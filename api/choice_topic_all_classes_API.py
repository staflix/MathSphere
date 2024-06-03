from flask import render_template, redirect
import flask
from forms.choice_topic_all_classes_Form import ChoiceTopicAllClassesForm
from forms.mainpageForm import LogMainPageForm
from data import db_session
from data.users import User, Info
from flask_login import current_user

blueprint = flask.Blueprint(
    'choicetopicallclasses_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/<int:num_class>', methods=['GET', 'POST'])
def choice_topic_all_classes_trainer(num_class):
    form = ChoiceTopicAllClassesForm()
    profile = LogMainPageForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.user_id == current_user.id).first()
    user_name = current_user.name
    user_surname = current_user.surname
    user_email = current_user.email
    user_avatar = f"../{user_info.avatar_href}"

    if num_class == 1:
        if form.topic11.data:
            topic = "Счет предметов"
            return redirect(f"/{num_class}/{topic}")

        if form.topic12.data:
            topic = "Многоугольники"
            return redirect(f"/{num_class}/{topic}")

        if form.topic13.data:
            topic = "Задачки на увеличение"
            return redirect(f"/{num_class}/{topic}")

        if form.topic14.data:
            topic = "Задачки на уменьшение"
            return redirect(f"/{num_class}/{topic}")

        if form.topic15.data:
            topic = "Задачки (разнобой)"
            return redirect(f"/{num_class}/{topic}")

        if form.topic16.data:
            topic = "Примеры на счет"
            return redirect(f"/{num_class}/{topic}")

    return render_template("choice_topic.html", num_class=num_class, form=form, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email)
