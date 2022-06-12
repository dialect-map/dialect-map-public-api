# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import g
from flask import jsonify

from dialect_map_core import MembershipController
from dialect_map_schemas import CategoryMembershipSchema


bp = Blueprint("memberships", __name__)


@bp.get("/category/membership/<membership_id>")
def get_membership(membership_id: str):
    """
    Category membership endpoint
    ---
    get:
      description: Get a category membership from the database
      parameters:
        - name: membership_id
          in: path
          description: Category membership identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: Category membership JSON record
          content:
            application/json:
              schema: CategoryMembershipSchema
    """

    controller = MembershipController(g.session)

    membership = controller.get(membership_id)
    schema = CategoryMembershipSchema()
    record = schema.dump(membership)

    return jsonify(record), 200


@bp.get("/category/membership/paper/<path:paper_id>/rev/<paper_rev>")
def get_membership_by_paper(paper_id: str, paper_rev: int):
    """
    Category memberships by paper endpoint
    ---
    get:
      description: Get a list of category memberships from the database
      parameters:
        - name: paper_id
          in: path
          description: ArXiv paper identifier
          required: true
          schema:
            type: string
        - name: paper_rev
          in: path
          description: ArXiv paper revision
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Category membership JSON records
          content:
            application/json:
              schema:
                type: array
                items: CategoryMembershipSchema
    """

    controller = MembershipController(g.session)

    memberships = controller.get_by_paper(paper_id, paper_rev)
    schemas = CategoryMembershipSchema(many=True)
    records = schemas.dump(memberships)

    return jsonify(records), 200
