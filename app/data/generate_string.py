from app.data import db_session
from app.data.users import Info
import random
import string


def generate_string():
    while True:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        random_string = '-'.join([random_string[i:i + 4] for i in range(0, len(random_string), 4)])

        db_session.global_init("db/MathSphereBase.db")
        db_sess = db_session.create_session()

        existing_info = db_sess.query(Info).filter(Info.random_string == random_string).first()
        db_sess.close()

        if not existing_info:
            return random_string
