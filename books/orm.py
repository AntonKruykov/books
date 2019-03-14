from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import settings

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(150))
    publish_year = Column(Integer)
    author = Column(String(150))
    pages_count = Column(Integer)
    create_dt = Column(DateTime(), default=datetime.utcnow)

    def dump(self):
        return dict([(k, v) for k, v in vars(self).items()
                     if not k.startswith('_')])


def init_db():
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI,
                           convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
