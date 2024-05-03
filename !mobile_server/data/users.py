from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import declarative_base
from sqlalchemy_serializer import SerializerMixin
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
        return f"{self.id}-{self.surname}-{self.name}-{self.age}-" \
               f"{self.profile_level}-{self.email}-{self.hashed_password}"
