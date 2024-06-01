from flask import render_template, redirect, request
import flask
from forms.settings_Form import SettingsForm
from data import db_session
from data.users import User, Info

blueprint = flask.Blueprint(
    'settings_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/settings/key=<rdm_string>', methods=['GET', 'POST'])
def settings(rdm_string):
    form = SettingsForm()
    next_page = request.args.get('next')

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()

    if form.next.data:
        if form.password.data == form.confirm_password.data:
            if form.name.data:
                user.name = form.name.data
            if form.surname.data:
                user.surname = form.surname.data
            if form.password.data:
                user.set_password(form.password.data)
            db_sess.commit()
            db_sess.close()
            if next_page == 'main_page':
                return redirect(f"/key={rdm_string}")
            elif next_page == 'company':
                return redirect(f"/menu_company/key={rdm_string}")
            elif next_page == 'choice_class':
                return redirect(f"/choice_class/key={rdm_string}")

        else:
            return render_template("settings.html", form=form,
                                   message="Пароли не совпадают", rdm_string=rdm_string, next_page=next_page)

    return render_template("settings.html", form=form, rdm_string=rdm_string, next_page=next_page)
