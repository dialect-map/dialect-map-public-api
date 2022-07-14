# -*- coding: utf-8 -*-

from flask_cors import CORS

from api.config import ApplicationConfig
from api.config import EnvironmentConfigLoader
from api.factory import create_app
from logs import setup_logger


# Gunicorn running the server
if __name__ == "main":

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    setup_logger(config.log_level)

    app = create_app(config.database_url)
    cors = CORS(app, methods=["GET"])


# Flask running the server
if __name__ == "__main__":

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    setup_logger(config.log_level)

    app = create_app(config.database_url)
    cors = CORS(app, methods=["GET"])
