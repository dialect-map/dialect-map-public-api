# -*- coding: utf-8 -*-

from flask_cors import CORS

from api.config import ApplicationConfig
from api.config import EnvironmentConfigLoader
from api.factory import create_app
from logs import setup_logger


if __name__ == "main":
    """Gunicorn running the server"""

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    setup_logger(config.log_level)

    app = create_app(config.database_url)
    cors = CORS(app, methods=["GET"])


if __name__ == "__main__":
    """Flask running the server"""

    loader = EnvironmentConfigLoader()
    config = ApplicationConfig(loader)

    setup_logger(config.log_level)

    app = create_app(config.database_url)
    cors = CORS(app, methods=["GET"])
