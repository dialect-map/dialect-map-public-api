# -*- coding: utf-8 -*-

from flask import Flask
from openapi_spec_validator import validate_v3_spec

from src.api.routes import all_blueprints
from src.api.routes import build_openapi_spec


def test_openapi_spec():
    """
    Tests the correct definition of OpenAPI 3.0 doc-strings
    Reference: https://swagger.io/specification/
    """

    app = Flask(__name__)

    # Setup all the blueprint routes
    for bp in all_blueprints:
        app.register_blueprint(bp)

    # Simulate a running application
    with app.app_context():
        validate_v3_spec(build_openapi_spec())
