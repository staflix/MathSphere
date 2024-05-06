# НУЖНО УСТАНОВИТЬ requirements.txt командой 'pip install -r requirements.txt'
from flask_login import LoginManager, login_required, logout_user
from flask import Flask, render_template, redirect
from forms.loginForm import LoginForm
from data import db_session
from data.users import User
from api import registerAPI, loginAPI, simplearithmeticAPI, resetpasswordAPI, mainpageAPI

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


# для верной работы flask-login
@login_manager.user_loader
def load_user(user_id):
    db_session.global_init("db/MathSphereBase.db")
    db_sess = db_session.create_session()
    return db_sess.get(User, user_id)


# выход с аккаунта, когда нажимаешь на имя
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


# выбор математичесих методов
@app.route('/trainer', methods=['GET', 'POST'])
def trainer():
    return render_template('trainer.html')


# обработка ошибки 404
@app.errorhandler(404)
def not_found_error(_):
    return render_template('404.html')


def main():
    app.register_blueprint(registerAPI.blueprint)
    app.register_blueprint(loginAPI.blueprint)
    app.register_blueprint(simplearithmeticAPI.blueprint)
    app.register_blueprint(resetpasswordAPI.blueprint)
    app.register_blueprint(mainpageAPI.blueprint)
    app.run(port=5000, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
