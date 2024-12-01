from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .api_views import init_app as api_init_app
    from .error_handlers import init_app as error_handlers_init_app
    from .models import URLMap
    from .views import init_app as views_init_app

    api_init_app(app)
    error_handlers_init_app(app)
    views_init_app(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()
