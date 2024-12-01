from http import HTTPStatus

from flask import render_template

from . import db


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {"message": self.message}


def init_app(app):
    @app.errorhandler(HTTPStatus.BAD_REQUEST)
    def handle_bad_request(error):
        return render_template('400.html'), HTTPStatus.BAD_REQUEST

    @app.errorhandler(HTTPStatus.NOT_FOUND)
    def page_not_found(error):
        return render_template('404.html'), HTTPStatus.NOT_FOUND

    @app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
