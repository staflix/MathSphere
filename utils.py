from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


# создание сессии, чтобы делать запросы, удобно юзать, ведь мы часто будем взаимодействовать с бд
def make_session():
    SqlAlchemyBase = declarative_base()
    engine = create_engine(f'sqlite:///db/MathSphereBase.db')
    SqlAlchemyBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
