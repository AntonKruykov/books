from datetime import datetime

from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base


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
