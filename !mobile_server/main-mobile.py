from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

test_user = []


@app.route("/")
def get_user_name():
    db_sess = db_session.create_session()

    for user in db_sess.query(User).all():
        test_user.append(user.name)
        print(user.name)

    return test_user


def main():
    db_session.global_init("../db/MathSphereBase.db")
    app.run()



if __name__ == '__main__':
    main()
