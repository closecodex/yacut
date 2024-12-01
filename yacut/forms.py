from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, Length, Regexp

MAX_SHORT_ID_LENGTH = 16


class URLForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(
                require_tld=True,
                message='Введите правильный URL'
            )
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                max=MAX_SHORT_ID_LENGTH,
                message=f'Максимальная длина {MAX_SHORT_ID_LENGTH} символов'
            ),
            Regexp(
                r'^[A-Za-z0-9]*$',
                message='Допустимы только латинские буквы и цифры'
            )
        ],
        filters=[lambda x: x or None]
    )
    submit = SubmitField('Укоротить')
