# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import make_response
from flask import request
from globals import service

from dialect_map.models import Category


bp = Blueprint("categories", __name__)


@bp.route("/category/<category_id>", methods=["GET"])
def get_category(category_id: str):
    """
    Gets a category from the underlying database
    :param category_id: ID of the category to get
    :return: HTTP 200 response
    """

    record = service.categories.get(category_id)
    return make_response(jsonify(record), 200)


@bp.route("/category", methods=["POST"])
def create_category():
    """
    Creates a category with the provided JSON body
    :return: HTTP 201 response
    """

    json = request.json
    cat = Category(**json)
    resp = service.categories.create(cat)
    return make_response({"id": resp}, 201)


@bp.route("/category/<category_id>", methods=["DELETE"])
def delete_category(category_id: str):
    """
    Deletes a category from the underlying database
    :param category_id: ID of the category to delete
    :return: HTTP 200 response
    """

    service.categories.delete(category_id)
    return make_response(jsonify({}), 204)
