# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
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
