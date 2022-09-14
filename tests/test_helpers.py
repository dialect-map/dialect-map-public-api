# -*- coding: utf-8 -*-

from openapi_spec_validator import validate_spec

from src.api.factory import create_app
from src.api.routes import build_openapi_spec


def test_openapi_spec():
    """
    Tests the correct definition of OpenAPI 3.0 doc-strings
    Reference: https://swagger.io/specification/
    """

    app = create_app("sqlite:///:memory:")

    # Simulate a running application
    with app.app_context():
        validate_spec(build_openapi_spec())
