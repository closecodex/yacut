from flask import Blueprint, render_template, redirect, url_for

from . import db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id

views_bp = Blueprint('views', __name__)


@views_bp.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data or get_unique_short_id()

        if URLMap.query.filter_by(short=custom_id).first():
            error_message = (
                'Предложенный вариант короткой ссылки уже существует.'
            )
            return render_template(
                'index.html', form=form, duplicated_error=error_message
            )

        new_link = URLMap(original=original_link, short=custom_id)
        db.session.add(new_link)
        db.session.commit()
        short_link = url_for(
            'views.redirect_short', short=custom_id, _external=True
        )
        return render_template(
            'index.html', form=form, short_link=short_link
        )

    return render_template('index.html', form=form)


@views_bp.route('/<string:short>', methods=['GET'])
def redirect_short(short):
    link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(link.original)
