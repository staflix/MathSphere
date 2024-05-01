# НУЖНО УСТАНОВИТЬ requirements.txt командой 'pip install -r requirements.txt'
from flask_login import LoginManager, login_user, login_required, logout_user
from flask import Flask, render_template, redirect
from forms.loginForm import LoginForm
from forms.registerForm import RegisterForm
from data import db_session
from sqlalchemy import select
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


# для верной работы flask-login
@login_manager.user_loader
def load_user(user_id):
    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


# выход с аккаунта, когда нажимаешь на имя
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# главная страница
@app.route('/')
def index():
    return render_template('index.html', title='MathSphere')


# регистрация с сохранением в бд, проверку на почту, проверку на совпадения пароля и его подтверждения
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.submit.data:
        user = User()
        user.surname = form.surname.data
        user.name = form.name.data
        user.surname = form.surname.data
        user.profile_level = 1
        user.email = form.email.data
        user.set_password(form.password.data)
        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='MathSphere', form=form)


# авторизация, если в бд есть пользователь с данной почтой и пароли совпадают
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.submit.data)
    if form.submit.data:
        print(1)
        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)
