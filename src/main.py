# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS
from config import ApplicationConfig
from config import EnvironmentConfigLoader
from globals import setup_service
from logs import setup_logger


app = Flask(__name__)
cors = CORS(app, methods=["GET"])


def setup_encoding():
    """ Setup the Flask encoding / decoding classes """

    from dialect_map.encoding import CustomJSONDecoder
    from dialect_map.encoding import CustomJSONEncoder

    app.json_decoder = CustomJSONDecoder
    app.json_encoder = CustomJSONEncoder


def setup_routes():
    """ Setup all the Flask blueprint routes """

    from routes import all_blueprints

    for bp in all_blueprints:
        app.register_blueprint(bp)


def setup_errors():
    """ Setup all the Flask exception handlers """

    from handlers import error_mappings

    for mapping in error_mappings:
        for error in mapping["errors"]:
            app.register_error_handler(error, mapping["handler"])


# Gunicorn running the server
if __name__ == "main":

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    # Setup the logger first
    setup_logger(config.log_level)
    setup_service(c=config)

    setup_encoding()
    setup_routes()
    setup_errors()


# Flask running the server
if __name__ == "__main__":

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    # Setup the logger first
    setup_logger(config.log_level)
    setup_service(c=config)

    setup_encoding()
    setup_routes()
    setup_errors()
