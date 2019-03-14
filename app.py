import connexion
from flask_cors import CORS

import settings

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('books.yaml')

CORS(app.app)

application = app.app


@application.teardown_appcontext
def shutdown_session(exception=None):
    from books.api import db_session
    db_session.remove() # close db connection correctly


if __name__ == '__main__':
    app.run(port=settings.PORT)
