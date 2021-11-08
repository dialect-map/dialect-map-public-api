# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS

from api.config import ApplicationConfig
from api.config import EnvironmentConfigLoader
from api.globals import setup_service
from logs import setup_logger


app = Flask(__name__)
cors = CORS(app, methods=["GET"])


def create_app():
    """Initializes the Flask application entity"""

    from api.handlers import clean_session
    from api.handlers import error_mappings
    from api.routes import all_blueprints

    # Setup all the blueprint routes
    for bp in all_blueprints:
        app.register_blueprint(bp)

    # Setup all the error handlers
    for mapping in error_mappings:
        for error in mapping["errors"]:
            app.register_error_handler(error, mapping["handler"])

    # Setup all the context handlers
    app.teardown_request(clean_session)


# Gunicorn running the server
if __name__ == "main":

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    setup_logger(config.log_level)
    setup_service(c=config)

    create_app()


# Flask running the server
if __name__ == "__main__":

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    setup_logger(config.log_level)
    setup_service(c=config)

    create_app()
