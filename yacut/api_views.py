import re
from http import HTTPStatus

from flask import jsonify, request

from . import db
from .models import URLMap
from .utils import get_unique_short_id


def init_app(app):
    @app.route('/api/id/', methods=['POST'])
    def add_short_link():
        data = request.get_json(silent=True)

        if not data:
            return jsonify(
                {'message': 'Отсутствует тело запроса'}
            ), HTTPStatus.BAD_REQUEST

        if not isinstance(data, dict):
            return jsonify(
                {'message': 'Невалидный JSON'}
            ), HTTPStatus.BAD_REQUEST

        if 'url' not in data:
            return jsonify(
                {'message': '"url" является обязательным полем!'}
            ), HTTPStatus.BAD_REQUEST

        original = data['url']
        custom_id = data.get('custom_id')

        if not custom_id:
            custom_id = get_unique_short_id()
        else:
            if not re.match(r'^[A-Za-z0-9]{1,16}$', custom_id):
                return jsonify(
                    {'message': 'Указано недопустимое имя для короткой ссылки'}
                ), HTTPStatus.BAD_REQUEST

            if URLMap.query.filter_by(short=custom_id).first():
                return jsonify(
                    {
                        'message': (
                            'Предложенный вариант короткой ссылки '
                            'уже существует.'
                        )
                    }
                ), HTTPStatus.BAD_REQUEST

        new_link = URLMap(original=original, short=custom_id)
        db.session.add(new_link)
        db.session.commit()

        return jsonify({
            'url': new_link.original,
            'short_link': f"{request.host_url.rstrip('/')}/{new_link.short}"
        }), HTTPStatus.CREATED

    @app.route('/api/id/<string:short>/', methods=['GET'])
    def get_original_link(short):
        link = URLMap.query.filter_by(short=short).first()
        if not link:
            return jsonify(
                {'message': 'Указанный id не найден'}
            ), HTTPStatus.NOT_FOUND

        return jsonify({'url': link.original}), HTTPStatus.OK
