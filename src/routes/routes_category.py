# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import request
from globals import service


bp = Blueprint("categories", __name__)


@bp.route("/category/<category_id>", methods=["GET"])
def get_category(category_id: str):
    """
    Gets a category from the underlying database
    :param category_id: ID of the category to get
    :return: HTTP 200 response
    """

    record = service.categories.get(category_id)
    return jsonify(record.data), 200


@bp.route("/category/all", methods=["GET"])
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

    records = service.categories.get_all(include_archived)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200
