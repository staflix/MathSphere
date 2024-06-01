from flask import render_template, redirect
import flask
from forms.choice_class_Form import ChoiceClassForm
from forms.mainpageForm import LogMainPageForm
from data import db_session
from data.users import User, Info

blueprint = flask.Blueprint(
    'choiceclass_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/choice_class/key=<rdm_string>', methods=['GET', 'POST'])
def choice_class(rdm_string):
    form = ChoiceClassForm()
    profile = LogMainPageForm()

    page = 'choice_class'

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    user_name = user.name
    user_surname = user.surname
    user_email = user.email
    user_avatar = f"../{user_info.avatar_href}"
    if form.first_class.data:
        return redirect(f"/1/key={rdm_string}")

    if form.second_class.data:
        return redirect(f"/2/key={rdm_string}")

    if form.third_class.data:
        return redirect(f"/3/key={rdm_string}")

    if form.fourth_class.data:
        return redirect(f"/4/key={rdm_string}")

    if profile.settings.data:
        return redirect(f"/settings/key={rdm_string}?next={page}")

    if profile.change_avatar.data:
        return redirect(f"/change_avatar/key={rdm_string}?next={page}")

    if profile.exit.data:
        return redirect(f"/logout")

    return render_template("choice_class.html", form=form, rdm_string=rdm_string, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email)
