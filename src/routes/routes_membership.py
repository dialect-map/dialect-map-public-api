# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from globals import service


bp = Blueprint("memberships", __name__)


@bp.route("/membership/<membership_id>", methods=["GET"])
def get_membership(membership_id: str):
    """
    Gets a membership from the underlying database
    :param membership_id: ID of the membership to get
    :return: HTTP 200 response
    """

    record = service.category_memberships.get(membership_id)
    return jsonify(record.data), 200
