from flask import render_template, redirect, request
import flask
from forms.settings_Form import SettingsForm
from data import db_session
from flask_login import current_user
from data.users import User

blueprint = flask.Blueprint(
    'settings_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    next_page = request.args.get('next')

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == current_user.id).first()

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
                return redirect(f"/")
            elif next_page == 'company':
                return redirect(f"/menu_company")
            elif next_page == 'choice_class':
                return redirect(f"/choice_class")
            elif 'choice_topic_all_classes_trainer' in next_page:
                return redirect(f"/{next_page.split(',')[-1]}")

        else:
            return render_template("settings.html", form=form,
                                   message="Пароли не совпадают", next_page=next_page)

    return render_template("settings.html", form=form, next_page=next_page)
