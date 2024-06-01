from flask import Flask, redirect, url_for, session, request
from urllib.parse import urlencode
import requests
from pprint import pprint
from flask import render_template, redirect
import flask
from data import db_session
from data.users import User, Info
from data.generate_string import generate_string
from api.resetpasswordAPI import generate_password
from mail import send_email
from forms.yandex_regForm import YandexForm

blueprint = flask.Blueprint(
    'yandex_api',
    __name__,
    template_folder='templates'
)

# Конфигурация Яндекс
CLIENT_ID = 'f07a1010e5a84481944dea7a07d12041'  # не трогать
CLIENT_SECRET = '64cd6f61c7c04e8c8af1dbd89ec8c3ea'  # не трогать
REDIRECT_URI = 'http://127.0.0.1:5000/login/callback'  # потом потрогаю
AUTH_URL = 'https://oauth.yandex.ru/authorize'
TOKEN_URL = 'https://oauth.yandex.ru/token'
USERINFO_URL = 'https://login.yandex.ru/info'


@blueprint.route('/reg_yandex', methods=['GET', 'POST'])
def reg_yandex():
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI
    }
    return redirect(f"{AUTH_URL}?{urlencode(params)}")


@blueprint.route('/login/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'код где?'

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }

    response = requests.post(TOKEN_URL, data=data)
    response_data = response.json()
    access_token = response_data.get('access_token')

    if not access_token:
        return 'токен гдн'

    user_info_response = requests.get(USERINFO_URL, params={'format': 'json', 'oauth_token': access_token})
    user_info = user_info_response.json()

    session['user'] = user_info
    return redirect('/profile')


@blueprint.route('/profile')
def profile():
    form = YandexForm()
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    user_table = db_sess.query(User).filter(User.email == user['emails'][0]).first()

    if user_table:
        user_info = db_sess.query(Info).filter(Info.user_id == user_table.id).first()
        new_random_string = generate_string()
        user_info.random_string = new_random_string
        db_sess.commit()
        db_sess.close()
        return redirect(f'/key={new_random_string}')

    if not user_table:
        new_user = User(
            surname=user['last_name'],
            name=user['first_name'],
            profile_level=1,
            email=user['emails'][0]
        )
        password = generate_password()
        send_email(user['emails'][0], 'Ваш пароль MathUp!',
                   f'Вы зарегистрировались с помощью своего яндекс аккаунта. Пароль: {password}')
        new_user.set_password(password)
        db_sess.add(new_user)
        db_sess.commit()
        db_sess.refresh(new_user)
        avatar = f'static/avatars_img/15.png'
        rdm_string = generate_string()
        info = Info(
            user_id=new_user.id,
            avatar_href=avatar,
            random_string=rdm_string,
            current_level=0
        )
        db_sess.add(info)
        db_sess.commit()
        db_sess.close()
        return redirect(f"/key={rdm_string}?reg=True")
