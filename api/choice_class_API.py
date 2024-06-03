from flask import render_template, redirect
import flask
from forms.choice_class_Form import ChoiceClassForm
from forms.mainpageForm import LogMainPageForm
from flask_login import current_user
from data import db_session
from data.users import Info

blueprint = flask.Blueprint(
    'choiceclass_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/choice_class', methods=['GET', 'POST'])
def choice_class():
    form = ChoiceClassForm()
    profile = LogMainPageForm()

    page = 'choice_class'

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.user_id == current_user.id).first()
    user_name = current_user.name
    user_surname = current_user.surname
    user_email = current_user.email
    user_avatar = f"../{user_info.avatar_href}"

    db_sess.close()

    if form.first_class.data:
        return redirect(f"/1")

    if form.second_class.data:
        return redirect(f"/2")

    if form.third_class.data:
        return redirect(f"/3")

    if form.fourth_class.data:
        return redirect(f"/4")

    if profile.settings.data:
        return redirect(f"/settings?next={page}")

    if profile.change_avatar.data:
        return redirect(f"/change_avatar?next={page}")

    if profile.exit.data:
        return redirect(f"/logout")

    return render_template("choice_class.html", form=form, profile=profile,
                           avatar=user_avatar, name=user_name, surname=user_surname,
                           email=user_email)
