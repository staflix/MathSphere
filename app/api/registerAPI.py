from flask import render_template, redirect
import flask
from sqlalchemy import select
from app.forms.registerForm import RegisterForm
from app.data import db_session
from app.data.users import User, Info
from app.check_email import is_valid_email
from app.data.generate_string import generate_string

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
                    # по умолчанию аватарка вот
                    avatar = 'https://i.ibb.co/C2WLdyY/avatar1.png'
                    rdm_string = generate_string()
                    info = Info(
                        user_id=user.id,
                        avatar_href=avatar,
                        random_string=rdm_string
                    )
                    db_sess.add(info)
                    db_sess.commit()
                    db_sess.close()
                    return redirect(f"/key={rdm_string}")
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
