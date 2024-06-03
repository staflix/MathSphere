from flask import render_template, redirect
import flask
from flask_login import login_user
from sqlalchemy import select
from forms.registerForm import RegisterForm
from data import db_session
from data.users import User, Info
from data.check_email import is_valid_email

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
            if is_valid_email(form.email.data):
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
                    db_sess.refresh(user)
                    avatar = f'static/avatars_img/15.png'
                    info = Info(
                        user_id=user.id,
                        avatar_href=avatar,
                        current_level=0
                    )
                    db_sess.add(info)
                    db_sess.commit()
                    db_sess.close()
                    login_user(user, remember=True)
                    return redirect(f"/")
                else:
                    return render_template('register.html',
                                           message='Пароли не совпадают', form=form)
            else:
                return render_template('register.html',
                                       message='Такой почты не существует',
                                       form=form)
        else:
            return render_template('register.html',
                                   message='Аккаунт с данной почтой уже существует',
                                   form=form)
    return render_template('register.html', form=form)
