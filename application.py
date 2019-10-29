from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(**config_overides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # Apply overrides for tests
    app.config.update(config_overides)

    # Initialize DB 
    db.init_app(app)
    migrate = Migrate(app, db)

    from counter.views import counter_app
    app.register_blueprint(counter_app)

    return app