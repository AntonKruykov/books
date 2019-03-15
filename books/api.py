from connexion import NoContent
from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy import and_, or_

from books.database import init_db
from books.models import Book, BookSchema

db_session = init_db()


def j(*args, **kwargs):
    """Wrapper around jsonify that sets the Content-Type of the response to
    application/vnd.api+json.
    """
    response = jsonify(*args, **kwargs)
    response.mimetype = 'application/vnd.api+json'
    return response


def get_books(filterauthor=None, filtertitle=None, filterdate_start=None,
              filterdate_end=None):

    conditions = []
    if filterauthor:
        conditions.append(Book.author.like('%{}%'.format(filterauthor)))
    if filtertitle:
        conditions.append(Book.title.like('%{}%'.format(filtertitle)))

    date_conditions = []
    if filterdate_start:
        date_conditions.append(Book.create_dt >= filterdate_start)
    if filterdate_end:
        date_conditions.append(Book.create_dt <= filterdate_end)

    q = db_session.query(Book)
    q = q.filter(or_(or_(*conditions), and_(*date_conditions)))

    data = BookSchema(many=True).dump(q).data
    return j(data)


def add_books(books):

    schema = BookSchema(many=True)
    try:
        data = schema.load(books).data
    except ValidationError as err:
        return j(err.messages), 422

    for book in data:
        db_session.add(Book(**book))
    db_session.commit()
    return NoContent, 201


def edit_book(id, book):
    b = db_session.query(Book).filter(Book.id == id).one_or_none()

    if b is None:
        return NoContent, 404

    schema = BookSchema()
    try:
        data = schema.load(book).data
    except ValidationError as err:
        return j(err.messages), 422

    db_session.query(Book).filter(Book.id == id).update(data)
    db_session.commit()
    return NoContent, 200


def delete_book(id):
    b = db_session.query(Book).filter(Book.id == id).one_or_none()
    if b is None:
        return NoContent, 404
    db_session.query(Book).filter(Book.id == id).delete()
    db_session.commit()
    return NoContent, 204
