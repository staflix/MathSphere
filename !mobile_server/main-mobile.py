from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("../db/MathSphereBase.db")
    db_sess = db_session.create_session()

    for user in db_sess.query(User).all():
        print(user.name)
    # app.run()


if __name__ == '__main__':
    main()
