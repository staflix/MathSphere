from flask import Flask, redirect, url_for, session, request
from urllib.parse import urlencode
import requests
from pprint import pprint

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'

# Конфигурация Яндекс
CLIENT_ID = 'f07a1010e5a84481944dea7a07d12041'  # не трогать
CLIENT_SECRET = '64cd6f61c7c04e8c8af1dbd89ec8c3ea'  # не трогать
REDIRECT_URI = 'http://127.0.0.1:5000/login/callback'  # потом потрогаю
AUTH_URL = 'https://oauth.yandex.ru/authorize'
TOKEN_URL = 'https://oauth.yandex.ru/token'
USERINFO_URL = 'https://login.yandex.ru/info'


@app.route('/')
def index():
    return '<a href="/login">login_Yandex</a>'


@app.route('/login')
def login():
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI
    }
    return redirect(f"{AUTH_URL}?{urlencode(params)}")


@app.route('/login/callback')
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
    return redirect(url_for('profile'))


@app.route('/profile')
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    pprint(user)
    return f"Привет, {user['real_name']}!"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
