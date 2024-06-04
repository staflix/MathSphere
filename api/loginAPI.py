from flask import render_template, redirect
import flask
from forms.loginForm import LoginForm
from data import db_session
from data.users import User, Info
from flask_login import login_user
from data.generate_string import generate_string

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
            info = db_sess.query(Info).filter(Info.user_id == user.id).first()
            if info:
                info.rdm_string = generate_string()
                db_sess.commit()
                rdm_string = info.rdm_string
                db_sess.close()
                return redirect(f'/login_password/key={rdm_string}')
            else:
                db_sess.close()
                return render_template('login_email.html',
                                       message="Информация о пользователе не найдена!", form=form)
        else:
            db_sess.close()
            return render_template('login_email.html',
                                   message="Аккаунта с такой почтой не существует!", form=form)
    return render_template('login_email.html', form=form)


@blueprint.route('/login_password/key=<rdm_string>', methods=['GET', 'POST'])
def login_password(rdm_string):
    form = LoginForm()

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()

    user_info = db_sess.query(Info).filter(Info.rdm_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    form.email.data = user.email
    db_sess.close()

    if form.validate_on_submit():

        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()

        if user:
            if user.check_password(form.password.data):
                login_user(user, remember=True)
                return redirect(f'/')
            else:
                db_sess.close()
                return render_template('login_password.html', form=form, message='Неправильный пароль',
                                       rdm_string=rdm_string)
        else:
            db_sess.close()
            return render_template('login_password.html', form=form, message='Такого аккаунта не существует',
                                   rdm_string=rdm_string)

    return render_template('login_password.html', form=form, rdm_string=rdm_string)
