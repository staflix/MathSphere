import flask
from app.forms.resetpasswordForm import ResetPasswordForm
from flask import render_template, redirect
from app.data import db_session
from app.data.users import User, Info
from app.mail import send_email

blueprint = flask.Blueprint(
    'resetpassword_api',
    __name__,
    template_folder='templates'
)


# потом напилить норм пароль, как у яндекса
def generate_password():
    return '12345'


@blueprint.route('/reset_password/key=<rdm_string>', methods=['POST', 'GET'])
def reset_password(rdm_string):
    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    user_id = db_sess.query(Info).filter(Info.random_string == rdm_string).first().user_id
    user = db_sess.query(User).filter(User.id == user_id).first()
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
        return redirect(f'/login/key={rdm_string}')

    return render_template('reset_password.html', form=form, email=user.email,
                           message_question=f'Сбросить пароль на аккаунте с почтой {user.email}?')
