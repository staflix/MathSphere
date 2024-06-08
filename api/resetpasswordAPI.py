import flask
from forms.resetpasswordForm import ResetPasswordForm
from flask import render_template, redirect
from data import db_session
from data.users import User, Info
from data.mail import send_email
import string
import random

blueprint = flask.Blueprint(
    'resetpassword_api',
    __name__,
    template_folder='templates'
)


def generate_password():
    length = 8
    all_characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(all_characters) for _ in range(length))

    has_digit = any(char.isdigit() for char in password)
    has_letter = any(char.isalpha() for char in password)

    while not (has_digit and has_letter):
        password = ''.join(random.choice(all_characters) for _ in range(length))
        has_digit = any(char.isdigit() for char in password)
        has_letter = any(char.isalpha() for char in password)

    return password


@blueprint.route('/reset_password/key=<rdm_string>', methods=['POST', 'GET'])
def reset_password(rdm_string):
    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    user_info = db_sess.query(Info).filter(Info.rdm_string == rdm_string).first()
    user = db_sess.query(User).filter(User.id == user_info.user_id).first()
    form = ResetPasswordForm()

    if form.submit.data:
        if user:
            new_password = generate_password()
            send_email(user.email, 'Сброс пароля MathUp!',
                       f'Ваш пароль на почту {user.email} был сброшен. Новый пароль: {new_password}')
            user.set_password(generate_password())
            email = user.email
            db_sess.commit()
            db_sess.close()
            return render_template('reset_password.html', form=form, email=email,
                                   message=f'Ваш пароль был сброшен. Новый пароль на почте {email}')

    if form.back.data:
        return redirect(f'/login_password/key={rdm_string}')

    return render_template('reset_password.html', form=form, email=user.email,
                           message_question=f'Сбросить пароль на аккаунте с почтой {user.email}?')
