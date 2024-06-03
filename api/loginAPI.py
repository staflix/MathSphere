from flask import render_template, redirect
import flask
from forms.loginForm import LoginForm
from data import db_session
from data.users import User
from flask_login import login_user

blueprint = flask.Blueprint(
    'login_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()

        user = db_sess.query(User).filter(User.email == form.email.data).first()

        db_sess.close()

        if user:

            if user.check_password(form.password.data):

                login_user(user, remember=True)
                return redirect(f'/')

            else:

                return render_template('login.html', form=form, message='Неправильный пароль')

        else:

            return render_template('login.html', form=form, message='Такого аккаунта не существует')

    return render_template('login.html', form=form)
