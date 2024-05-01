# НУЖНО УСТАНОВИТЬ requirements.txt командой 'pip install -r requirements.txt'
from flask_login import LoginManager, login_user, login_required, logout_user
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask import Flask, render_template, redirect
from forms.loginForm import LoginForm
from forms.registerForm import RegisterForm
from data import db_session
from sqlalchemy import select
from data.users import User
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

flag, status, num1, num2, example, answer = True, None, None, None, None, None


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
    return render_template('index.html')


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


# выбор математичесих методов
@app.route('/trainer', methods=['GET', 'POST'])
def trainer():
    return render_template('trainer.html')


@app.route('/simple_arithmetic', methods=['GET', 'POST'])
def simple_arithmetic():
    # добавить уровни
    global flag, status, num1, num2, example, answer
    form = SimpleArithmeticForm()
    if flag:
        num1 = str(random.randint(1, 10))
        num2 = str(random.randint(1, 10))
        example = str(num1) + '+' + str(num2) + '=?'
        answer = str(eval(f'{num1} + {num2}'))
        status = 'Не решено'
        flag = False
    else:
        if status == 'Решено верно!':
            if form.next.data:
                status = 'Не решено'
                num1 = str(random.randint(1, 10))
                num2 = str(random.randint(1, 10))
                example = str(num1) + '+' + str(num2) + '=?'
                answer = str(eval(f'{num1} + {num2}'))
    if form.check.data:
        if form.answer.data == answer:
            status = 'Решено верно!'
            return render_template('simple_arithmetic.html', example=example, status=status, form=form)
        elif form.answer.data != answer:
            status = 'Решено неверно!'
            return render_template('simple_arithmetic.html', example=example, status=status, form=form)
    return render_template('simple_arithmetic.html', example=example, status=status, form=form)


# форма для логина
class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


# форма для регистрации
class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_confirmation = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')


# форма менюшки
class MenuForm(FlaskForm):
    trainer = SubmitField('Тренажер', validators=[DataRequired()])
    # здесь добавить кнопочки меню


# форма тренажера
class TrainerForm(FlaskForm):
    simple_arithmetic = SubmitField('Простая арифметика', validators=[DataRequired()])  # пример 23 + 43 =
    # здесь добавить разные виды математических действий


# форма для режима простая арифметика
class SimpleArithmeticForm(FlaskForm):
    answer = StringField('Ответить', validators=[DataRequired()])
    check = SubmitField('Проверить')
    next = SubmitField('Продолжить')


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1', debug=True)
