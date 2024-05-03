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

message = 'почта'


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    global message, email
    form = LoginForm()

    if form.input_password.data:

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        db_sess.close()

        if user:
            message = 'пароль'
            email = form.email.data
            return render_template('login.html', message_mode='пароль',
                                   form=form, email=email)
        else:
            return render_template('login.html',
                                   message="Аккаунта с такой почтой не существует!",
                                   message_mode='пароль', form=form, email=email)
    if form.submit.data:

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == email).first()
        db_sess.close()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")

        else:
            render_template('login.html', form=form, message='Неправильный пароль',
                            message_mode='пароль',
                            email=email)

    return render_template('login.html', form=form, message_mode='почта')
