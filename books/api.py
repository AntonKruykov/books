from connexion import NoContent
from sqlalchemy import and_, or_

from books import orm

db_session = orm.init_db()


def get_books(author=None, title=None, date_start=None, date_end=None):

    conditions = []
    if author:
        conditions.append(orm.Book.author.like('%{}%'.format(author)))
    if title:
        conditions.append(orm.Book.title.like('%{}%'.format(title)))

    date_conditions = []
    if date_start:
        date_conditions.append(orm.Book.create_dt >= date_start)
    if date_end:
        date_conditions.append(orm.Book.create_dt <= date_end)

    q = db_session.query(orm.Book)
    q = q.filter(or_(or_(*conditions), and_(*date_conditions)))

    return [b.dump() for b in q]


def add_books(books):
    for book in books:
        db_session.add(orm.Book(**book))
    db_session.commit()
    return NoContent, 201


def edit_book(id, book):
    b = db_session.query(orm.Book).filter(orm.Book.id == id).one_or_none()
    if b is None:
        return NoContent, 404
    # todo explore update
    db_session.query(orm.Book).filter(orm.Book.id == id).update(book)
    db_session.commit()
    return NoContent, 200


def delete_book(id):
    b = db_session.query(orm.Book).filter(orm.Book.id == id).one_or_none()
    if b is None:
        return NoContent, 404
    db_session.query(orm.Book).filter(orm.Book.id == id).delete()
    db_session.commit()
    return NoContent, 204
