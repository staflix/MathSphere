from flask import render_template, redirect
import flask
from sqlalchemy import select
from forms.registerForm import RegisterForm
from data import db_session
from data.users import User

blueprint = flask.Blueprint(
    'register_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        query = select(User).filter(User.email == form.email.data)
        existing_user = db_sess.execute(query).fetchone()
        db_sess.close()
        if not existing_user:
            if form.password.data == form.password_confirmation.data:
                user = User(
                    surname=form.surname.data,
                    name=form.name.data,
                    profile_level=1,
                    email=form.email.data
                )
                user.set_password(form.password.data)
                db_sess.add(user)
                db_sess.commit()
                db_sess.close()
                return redirect("/")
            else:
                return render_template('register.html', title='MathSphere',
                                       message_password='Пароли не совпадают', form=form)
        else:
            return render_template('register.html', title='MathSphere',
                                   message_email='Аккаунт с данной почтой уже существует', form=form)
    return render_template('register.html', title='MathSphere', form=form)
