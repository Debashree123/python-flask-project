from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate
db=SQLAlchemy()
migrate=Migrate()

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # from .error import errors as error_bluprint
    # app.register_blueprint(error_bluprint)

    return app