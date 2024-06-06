from flask import url_for, session, request
from urllib.parse import urlencode
import requests
from flask import redirect
import flask
from data import db_session
from data.users import User, Info, TrainerStatistics
from api.resetpasswordAPI import generate_password
from data.mail import send_email
from data.config import *
from flask_login import login_user
from data.generate_string import generate_string
from data.tools import classes, topics

blueprint = flask.Blueprint(
    'yandex_api',
    __name__,
    template_folder='templates'
)

# Конфигурация Яндекс
CLIENT_ID = client_id  # не трогать
CLIENT_SECRET = client_secret  # не трогать
REDIRECT_URI = redirect_url  # потом потрогаю
AUTH_URL = auth_url
TOKEN_URL = token_url
USERINFO_URL = userinfo_url


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
    user = session.get('user')

    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    user_table = db_sess.query(User).filter(User.email == user['emails'][0]).first()

    if user_table:
        login_user(user_table, remember=True)
        db_sess.close()
        return redirect(f'/')

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
        info = Info(
            user_id=new_user.id,
            avatar_href=avatar,
            current_level=0,
            rdm_string=generate_string()
        )
        db_sess.add(info)

        for i in range(len(classes)):
            for j in range(len(topics[i])):
                num_class = classes[i]
                topic = topics[i][j]
                trainer = TrainerStatistics(
                    user_id=user.id,
                    num_class=num_class,
                    topic=topic
                )
                db_sess.add(trainer)
                db_sess.commit()

        login_user(new_user, remember=True)
        db_sess.close()
        return redirect(f"/?reg=True")
