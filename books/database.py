from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import settings
from books.models import Base


def init_db():
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI,
                           convert_unicode=True)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session