# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

from dialect_map_schemas import CategoryMembershipSchema

from ..globals import service


bp = Blueprint("memberships", __name__)


@bp.get("/category/membership/<membership_id>")
def get_membership(membership_id: str):
    """
    Gets a membership from the underlying database
    :param membership_id: ID of the membership to get
    :return: HTTP 200 response
    """

    member = service.category_memberships.get(membership_id)
    schema = CategoryMembershipSchema()
    record = schema.dump(member)

    return jsonify(record), 200


@bp.get("/category/membership/paper/<path:paper_id>/rev/<paper_rev>")
def get_membership_by_paper(paper_id: str, paper_rev: int):
    """
    Gets a list of memberships from the underlying database
    :param paper_id: ID of the paper to filter memberships by
    :param paper_rev: revision of the paper to filter memberships by
    :return: HTTP 200 response
    """

    members = service.category_memberships.get_by_paper(paper_id, paper_rev)
    schemas = CategoryMembershipSchema(many=True)
    records = schemas.dump(members)

    return jsonify(records), 200
