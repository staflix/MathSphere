from flask_mail import Message, Mail
import flask
from flask import request
from forms.resetpasswordForm import ResetPasswordForm
from flask import render_template, redirect
from data import db_session
from data.users import User
from sqlalchemy import select
from flask import url_for
from mail import send_email

blueprint = flask.Blueprint(
    'resetpassword_api',
    __name__,
    template_folder='templates'
)

email = None


# потом напилить норм пароль, как у яндекса
def generate_password():
    return '12345'


@blueprint.route('/reset_password', methods=['POST', 'GET'])
def reset_password():
    global email
    if request.method == 'GET':
        email = request.args.get('email')
    form = ResetPasswordForm()
    form.email.data = email

    if form.submit.data:
        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        query = select(User).filter(User.email == form.email.data)
        user = db_sess.execute(query).scalar_one_or_none()

        if user:
            new_password = generate_password()
            send_email(form.email.data, 'Сброс пароля MathUp!',
                       f'Ваш пароль на почту {form.email.data} был сброшен. Новый пароль: {new_password}')

            user.set_password(new_password)
            db_sess.commit()
            db_sess.close()

            return render_template('reset_password.html',
                                   message='Ваш пароль был изменён. Новый пароль был отправлен на почту!', form=form)
        else:
            db_sess.close()
            return render_template('reset_password.html',
                                   message='Аккаунта с такой почтой не существует', form=form)

    if form.back.data:
        return redirect('/login')

    return render_template('reset_password.html', form=form, email=email)
