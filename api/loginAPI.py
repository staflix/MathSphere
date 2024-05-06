from flask import render_template, redirect
import flask
from forms.loginForm import LoginForm
from flask_login import login_user
from data import db_session
from data.users import User

blueprint = flask.Blueprint(
    'login_api',
    __name__,
    template_folder='templates'
)

email = None


@blueprint.route('/login', methods=['GET', 'POST'])
def login_email():
    global email
    form = LoginForm()

    if form.input_password.data:

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        db_sess.close()

        if user:

            email = user.email
            return redirect('/login/password')

        else:

            return render_template('login.html',
                                   message="Аккаунта с такой почтой не существует!", form=form)

    return render_template('login.html', form=form)


@blueprint.route('/login/password', methods=['GET', 'POST'])
def login_password():
    global email
    form = LoginForm()
    form.email.data = email

    if form.validate_on_submit():

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == email).first()
        db_sess.close()

        if user and user.check_password(form.password.data):

            login_user(user, remember=form.remember_me.data)
            return redirect("/")

        else:
            return render_template('login_password.html', form=form, message='Неправильный пароль'
                                   , email=email)

    return render_template('login_password.html', form=form, email=email)
