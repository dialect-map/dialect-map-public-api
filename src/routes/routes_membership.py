# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from globals import service


bp = Blueprint("memberships", __name__)


@bp.route("/category/membership/<membership_id>", methods=["GET"])
def get_membership(membership_id: str):
    """
    Gets a membership from the underlying database
    :param membership_id: ID of the membership to get
    :return: HTTP 200 response
    """

    record = service.category_memberships.get(membership_id)
    return jsonify(record.data), 200


@bp.route("/category/membership/paper/<path:paper_id>/rev/<paper_rev>", methods=["GET"])
def get_membership_by_paper(paper_id: str, paper_rev: int):
    """
    Gets a list of memberships from the underlying database
    :param paper_id: ID of the paper to filter memberships by
    :param paper_rev: revision of the paper to filter memberships by
    :return: HTTP 200 response
    """

    records = service.category_memberships.get_by_paper(paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200
