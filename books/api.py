from connexion import NoContent

from books import orm

db_session = orm.init_db()


def get_books(author=None, title=None, date_start=None, date_end=None):
    q = db_session.query(orm.Book)
    # todo: explore complicated queries building
    # make q(author) OR q(title) OR q(date_start) AND q(date_end)
    if author:
        q = q.filter(orm.Book.author.like('%{}%'.format(author)))
    if title:
        q = q.filter(orm.Book.title.like('%{}%'.format(title)))
    if date_start:
        q = q.filter(orm.Book.create_dt >= date_start)
    if date_end:
        q = q.filter(orm.Book.create_dt <= date_end)
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
