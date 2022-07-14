# -*- coding: utf-8 -*-

import atexit
import logging

from flask import Flask

from .handlers import create_session
from .handlers import remove_session
from .handlers import error_mappings
from .globals import create_database
from .routes import all_blueprints


def _register_blueprints(app: Flask) -> None:
    """
    Registers all the blueprints into the Flask application
    :param app: Flask application object
    """

    for bp in all_blueprints:
        app.register_blueprint(bp)

    try:
        from api.routes import blueprint_help
    except ImportError:
        logging.info("Skipping API help endpoint")
    else:
        logging.info("Loading API help endpoint")
        app.register_blueprint(blueprint_help)


def _register_error_handlers(app: Flask) -> None:
    """
    Registers all the error handlers into the Flask application
    :param app: Flask application object
    """

    for mapping in error_mappings:
        for error in mapping.errors:
            app.register_error_handler(error, mapping.handler)


def _register_context_handlers(app: Flask) -> None:
    """
    Registers all the error handlers into the Flask applications
    :param app: Flask application object
    """

    app.before_request(create_session)
    app.after_request(remove_session)


def create_app(connection_url: str) -> Flask:
    """
    Initializes the Flask application object
    :param connection_url: database connection URL
    :return: Flask application object
    """

    app = Flask(__name__)

    database = create_database(connection_url)

    # The global entities must be stored first
    app.extensions["database"] = database

    _register_blueprints(app)
    _register_error_handlers(app)
    _register_context_handlers(app)

    # Register the database cleanup function upon exiting
    atexit.register(database.close_connection)

    return app
