# -*- coding: utf-8 -*-

from functools import lru_cache
from pathlib import Path

from apispec.core import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from flask import Blueprint
from flask import current_app
from flask import jsonify


bp = Blueprint("help", __name__)


def _get_all_routes() -> list:
    """
    Get all exportable routes from the current application object
    :return: list of route name and func tuples
    """

    routes = current_app.view_functions.items()
    routes = [r for r in routes if r[0].startswith("help") is False]
    routes = [r for r in routes if r[0].startswith("static") is False]

    return routes


def _get_spec_object() -> APISpec:
    """
    Creates an APISpec object with the API basic information
    :return: APISpec object
    """

    project_path = Path(__file__).parent.parent.parent.parent
    version_path = project_path / "VERSION"
    version_value = open(version_path).read().strip()

    return APISpec(
        title="Dialect-map Public API",
        version=version_value,
        openapi_version="3.0.2",
        plugins=[FlaskPlugin(), MarshmallowPlugin()],
    )


@lru_cache(maxsize=1)
def build_openapi_spec() -> dict:
    """
    Builds the OpenAPI specification for all the endpoints
    Reference: https://swagger.io/specification/
    :return: API specification dictionary
    """

    spec = _get_spec_object()

    for name, func in _get_all_routes():
        spec.path(view=func)

    return spec.to_dict()


@bp.get("/help")
def get_openapi_spec():
    """
    Gets the OpenAPI specification for all the endpoints
    :return: HTTP 200 response
    """

    return jsonify(build_openapi_spec()), 200
