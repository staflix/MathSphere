from flask import render_template, redirect
import flask
from app.forms.loginForm import LoginForm
from flask_login import login_user
from app.data import db_session
from app.data.users import User, Info
from app.data.generate_string import generate_string

blueprint = flask.Blueprint(
    'login_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/login', methods=['GET', 'POST'])
def login_email():
    form = LoginForm()

    if form.input_password.data:

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user:

            rdm_string = db_sess.query(Info).filter(Info.user_id == user.id).first()
            return redirect(f'/login/key={rdm_string.random_string}')

        else:

            return render_template('login_email.html',
                                   message="Аккаунта с такой почтой не существует!", form=form)

    return render_template('login_email.html', form=form)


@blueprint.route('/login/key=<rdm_string>', methods=['GET', 'POST'])
def login_password(rdm_string):
    form = LoginForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.random_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    form.email.data = user.email
    db_sess.close()

    if form.validate_on_submit():

        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()

        if user:
            if user.check_password(form.password.data):
                user_id = user.id
                new_random_string = generate_string()

                db_sess.query(Info).filter(Info.user_id == user_id).update({'random_string': new_random_string})
                db_sess.commit()

                db_sess.refresh(user)

                db_sess.close()

                login_user(user, remember=form.remember_me.data)
                return redirect(f'/key={new_random_string}')
            else:
                db_sess.close()
                return render_template('login_password.html', form=form, message='Неправильный пароль',
                                       rdm_string=rdm_string)
        else:
            db_sess.close()
            return render_template('login_password.html', form=form, message='Такого аккаунта не существует',
                                   rdm_string=rdm_string)

    return render_template('login_password.html', form=form, rdm_string=rdm_string)
