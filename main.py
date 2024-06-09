# НУЖНО УСТАНОВИТЬ requirements.txt командой 'pip install -r requirements.txt'
from flask_login import LoginManager, login_required, logout_user
from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.config import *
from api import registerAPI, loginAPI, resetpasswordAPI, mainpageAPI, choice_class_API, choice_topic_all_classes_API, \
    send_task_for_trainer_API, menu_company_API, change_avatar_API, settings_API, start_level_API, reg_log_yandexAPI, \
    mix_API
from flask import Flask, request, jsonify
from flask_login import current_user
import hashlib
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = key

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


@app.route('/save_result', methods=['POST'])
def save_result():
    md5_hash = hashlib.new('md5')
    md5_hash.update(current_user.email.encode())
    local_time = time.gmtime(time.time())
    t = local_time[:5]
    if 'action' in request.form:
        action = request.form['action']
        topic = request.form['topic']
        if action == 'start':
            num_class = request.form['num_class']
            with open(f'history/{md5_hash.hexdigest()}.txt', 'a', encoding='utf-8') as f:
                f.write(f'{str(t[2]).rjust(2, "0")}.{str(t[1]).rjust(2, "0")}.{t[0]} - {t[3]}:{t[4]} UTC \n'
                        f'Начало попытки. Класс {num_class}, Тема {topic}.\n')
        if action == 'add':
            num_class = request.form['num_class']
            result = request.form['result']
            with open(f'history/{md5_hash.hexdigest()}.txt', 'a', encoding='utf-8') as f:
                f.write(f"Класс {num_class}, Тема '{topic}', Вердикт {result}.\n")
        if action == 'end':
            with open(f'history/{md5_hash.hexdigest()}.txt', 'a', encoding='utf-8') as f:
                t = request.form['time'].split(':')
                t = round(int(t[0]) + int(t[1]) / 60, 2)
                correct = int(request.form['correct_answers'])
                summary = int(request.form['total_questions'])
                if summary != 0:
                    f.write(
                        f"Конец попытки.  Точность ответов {round((correct / summary) * 100, 2)}%, Затраченное время: {t} мин,"
                        f"\nСредняя скорость дачи правильных ответов: {round(correct / t, 2)} отв/мин.\n")
                else:
                    f.write(f"Конец попытки. Вы не ответили ни разу.\n")
    else:
        topic = request.json['topic']
        with open(f'history/{md5_hash.hexdigest()}.txt', 'a', encoding='utf-8') as f:
            f.write(f'{str(t[2]).rjust(2, "0")}.{str(t[1]).rjust(2, "0")}.{t[0]} - {t[3]}:{t[4]} UTC \n'
                    f'Начало попытки. Режим микс. Темы: {", ".join(topic)}.\n')
    return jsonify(success=True)


# обработка ошибки 404
@app.errorhandler(404)
def not_found_error(_):
    return render_template('404.html')


def main():
    app.register_blueprint(registerAPI.blueprint)
    app.register_blueprint(loginAPI.blueprint)
    app.register_blueprint(resetpasswordAPI.blueprint)
    app.register_blueprint(mainpageAPI.blueprint)
    app.register_blueprint(choice_class_API.blueprint)
    app.register_blueprint(choice_topic_all_classes_API.blueprint)
    app.register_blueprint(send_task_for_trainer_API.blueprint)
    app.register_blueprint(menu_company_API.blueprint)
    app.register_blueprint(change_avatar_API.blueprint)
    app.register_blueprint(settings_API.blueprint)
    app.register_blueprint(start_level_API.blueprint)
    app.register_blueprint(reg_log_yandexAPI.blueprint)
    app.register_blueprint(mix_API.blueprint)
    app.run(port=5000, host='127.0.0.1', debug=True)


if __name__ == '__main__':
    main()
