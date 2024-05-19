from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_serializer import SerializerMixin
from data import db_session
from sqlalchemy import ForeignKey
import sqlalchemy

SqlAlchemyBase = declarative_base()


# таблица пользователей
class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = "Users"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    profile_level = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f"{self.id}-{self.surname}-{self.name}-" \
               f"{self.profile_level}-{self.email}-{self.hashed_password}"


class Info(SqlAlchemyBase):
    __tablename__ = "Information"

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey("Users.id"))
    avatar_href = sqlalchemy.Column(sqlalchemy.String)
    random_string = sqlalchemy.Column(sqlalchemy.String)

    user = relationship("User")

    def __repr__(self):
        return f"{self.id}-{self.user_id}-{self.random_string}"


def clear_and_create_tables(db_file):
    engine = sqlalchemy.create_engine(f'sqlite:///{db_file.strip()}?check_same_thread=False')
    SqlAlchemyBase.metadata.create_all(engine)

    # Инициализация соединения с базой данных
    db_session.global_init(db_file)

    # Создание сессии
    db_sess = db_session.create_session()

    # Проверка существования таблицы Info и ее создание, если не существует
    if not table_exists(engine, "Info"):
        Info.__table__.create(engine)

    # Очистка всех записей из таблицы User
    db_sess.query(User).delete()

    # Сохранение изменений в базе данных
    db_sess.commit()


# Определяем функцию для проверки существования таблицы
def table_exists(engine, table_name):
    inspector = sqlalchemy.inspect(engine)
    return inspector.has_table(table_name)


def clear_users_table(db_file):
    engine = sqlalchemy.create_engine(f'sqlite:///{db_file.strip()}?check_same_thread=False')
    SqlAlchemyBase.metadata.create_all(engine)

    # Инициализация соединения с базой данных
    db_session.global_init(db_file)

    # Создание сессии
    db_sess = db_session.create_session()

    # Очистка всех записей из таблицы User
    db_sess.query(User).delete()

    # Сохранение изменений в базе данных
    db_sess.commit()


# clear_and_create_tables("db/MathSphereBase.db")
