from flask import render_template, redirect
import flask
from app.forms.settings_Form import SettingsForm
from app.data import db_session
from app.data.users import User, Info

blueprint = flask.Blueprint(
    'settings_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/settings/key=<rdm_string>', methods=['GET', 'POST'])
def settings(rdm_string):
    form = SettingsForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()

    form2 = SettingsForm()

    if form2.next.data:
        if form2.password.data == form2.confirm_password.data:
            if form2.name.data:
                user.name = form2.name.data
            if form2.surname.data:
                user.surname = form2.surname.data
            if form2.password.data:
                user.set_password(form2.password.data)
            db_sess.commit()
            db_sess.close()
            return redirect(f"/key={rdm_string}")
        else:
            return render_template("settings.html", form=form,
                                   message="Пароли не совпадают", rdm_string=rdm_string)

    return render_template("settings.html", form=form, rdm_string=rdm_string)
