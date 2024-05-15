from flask import render_template, redirect
from forms.mainpageForm import UnLogMainPageForm, LogMainPageForm
from flask_login import login_user
from data import db_session
from data.users import User, Info
import flask

blueprint = flask.Blueprint(
    'main_page_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/', methods=['GET', 'POST'])
def main_page_unlog():
    form = UnLogMainPageForm()
    return render_template('unlog_index.html', form=form)


# главная страница для зарегестрированного пользователя
@blueprint.route('/key=<rdm_string>', methods=['GET', 'POST'])
def main_page_log(rdm_string):
    form = LogMainPageForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    user_name = user.name
    user_surname = user.surname
    user_email = user.email
    user_avatar = user_info.avatar_href

    if form.settings.data:
        return redirect(f"/settings/key={rdm_string}")

    if form.change_avatar.data:
        return redirect(f"/change_avatar/key={rdm_string}")

    if form.exit.data:
        return redirect(f"/")

    if form.trainer_btn.data:
        return redirect(f"/choice_class/key={rdm_string}")

    if form.company_btn.data:
        return redirect(f"/menu_company/key={rdm_string}")

    return render_template('log_index.html', name=user_name, surname=user_surname,
                           email=user_email, avatar=user_avatar, form=form)
