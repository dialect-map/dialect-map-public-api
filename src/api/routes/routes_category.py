# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import request

from dialect_map_schemas import CategorySchema

from ..globals import service


bp = Blueprint("categories", __name__)


@bp.get("/category/<category_id>")
def get_category(category_id: str):
    """
    Gets a category from the underlying database
    :param category_id: ID of the category to get
    :return: HTTP 200 response
    """

    category = service.categories.get(category_id)
    schema = CategorySchema()
    record = schema.dump(category)

    return jsonify(record), 200


@bp.get("/category/all")
def get_category_all():
    """
    Gets all categories from the underlying database
    :return: HTTP 200 response
    """

    include_archived = request.args.get(
        key="archived",
        type=bool,
        default=False,
    )

    categories = service.categories.get_all(include_archived)
    schemas = CategorySchema(many=True)
    records = schemas.dump(categories)

    return jsonify(records), 200
