from flask_login import UserMixin
from sqlalchemy.orm import declarative_base
from sqlalchemy_serializer import SerializerMixin
import sqlalchemy
from utils import make_session

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

    def __repr__(self):
        return f"{self.id}-{self.surname}-{self.name}-{self.age}-" \
               f"{self.profile_level}-{self.email}-{self.hashed_password}"


# создание объекта в таблицу
session = make_session()

# user = User()
# user.surname = 'Nazarov'
# user.name = 'Nazar'
# user.profile_level = '1'
# user.email = 'nazar_nazarov_84@list.ru'
# user.hashed_password = 'zxc'

# session.add(user)

session.commit()
session.close()
