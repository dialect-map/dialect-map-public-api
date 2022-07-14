# -*- coding: utf-8 -*-

from flask import g

from src.api.factory import create_app


def test_application_creation():
    """Tests the correct initialization of app context functions"""

    app = create_app("sqlite:///:memory:")

    # Simulate a request context
    with app.test_request_context():
        app.preprocess_request()

        assert "database" in app.extensions
        assert "session" in g
