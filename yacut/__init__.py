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

    from .api_views import api_bp
    from .error_handlers import init_app as error_handlers_init_app
    from .views import views_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(views_bp)

    error_handlers_init_app(app)

    return app


app = create_app()
