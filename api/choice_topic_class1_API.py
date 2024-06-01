from flask import render_template, redirect
import flask
from forms.choice_topic_class1_Form import ChoiceTopicClass1Form
from forms.mainpageForm import LogMainPageForm
from data import db_session
from data.users import User, Info

blueprint = flask.Blueprint(
    'choicetopicclass1_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/<int:num_class>/key=<rdm_string>', methods=['GET', 'POST'])
def choice_topic_class1(num_class, rdm_string):
    form = ChoiceTopicClass1Form()
    profile = LogMainPageForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    user_name = user.name
    user_surname = user.surname
    user_email = user.email
    user_avatar = f"../{user_info.avatar_href}"

    if form.topic1.data:
        topic = "Счет предметов"
        return redirect(f"/{num_class}/{topic}/key={rdm_string}")

    return render_template("choice_topic.html", num_class=num_class, form=form, rdm_string=rdm_string, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email)
