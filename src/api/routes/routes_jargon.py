# -*- coding: utf-8 -*-

from urllib import parse

from flask import Blueprint
from flask import g
from flask import jsonify
from flask import request

from dialect_map_core import JargonController
from dialect_map_core import JargonGroupController
from dialect_map_schemas import JargonSchema
from dialect_map_schemas import JargonGroupSchema


bp = Blueprint("jargons", __name__)


# ------------------- Jargon model ------------------- #


@bp.get("/jargon/<jargon_id>")
def get_jargon(jargon_id: str):
    """
    Jargon term endpoint
    ---
    get:
      description: Get a jargon term from the database
      parameters:
        - name: jargon_id
          in: path
          description: Jargon term identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: Jargon term JSON record
          content:
            application/json:
              schema: JargonSchema
    """

    controller = JargonController(g.session)

    jargon = controller.get(jargon_id)
    schema = JargonSchema()
    record = schema.dump(jargon)

    return jsonify(record), 200


@bp.get("/jargon/all")
def get_jargon_all():
    """
    All jargon terms endpoint
    ---
    get:
      description: Get all jargon terms from the database
      parameters:
        - name: archived
          in: query
          description: Flag to whether or not include archived terms
          required: false
          schema:
            type: boolean
      responses:
        200:
          description: Jargon term JSON records
          content:
            application/json:
              schema:
                type: array
                items: JargonSchema
    """

    include_archived = request.args.get(
        key="archived",
        type=bool,
        default=False,
    )

    controller = JargonController(g.session)

    jargons = controller.get_all(include_archived)
    schemas = JargonSchema(many=True)
    records = schemas.dump(jargons)

    return jsonify(records), 200


@bp.get("/jargon/string/<jargon_str>")
def get_jargon_by_string(jargon_str: str):
    """
    Jargon term by string endpoint
    ---
    get:
      description: Get a jargon term from the database
      parameters:
        - name: jargon_str
          in: path
          description: Jargon term string
          required: true
          schema:
            type: string
      responses:
        200:
          description: Jargon term JSON record
          content:
            application/json:
              schema: JargonSchema
        404:
          description: Jargon term not found
    """

    controller = JargonController(g.session)

    string = parse.unquote(jargon_str)
    string = string.lower()

    jargon = controller.get_by_string(string)

    if jargon:
        schema = JargonSchema()
        record = schema.dump(jargon)
        return jsonify(record), 200
    else:
        return jsonify({}), 404


@bp.get("/jargon/group/<group_id>")
def get_jargon_by_group(group_id: str):
    """
    Jargon term by group endpoint
    ---
    get:
      description: Get a list of jargon terms from the database
      parameters:
        - name: group_id
          in: path
          description: Jargon terms group identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: Jargon term JSON records
          content:
            application/json:
              schema:
                type: array
                items: JargonSchema
    """

    controller = JargonController(g.session)

    jargons = controller.get_by_group(group_id)
    schemas = JargonSchema(many=True)
    records = schemas.dump(jargons)

    return jsonify(records), 200


# ---------------- Jargon Group model ---------------- #


@bp.get("/jargon-group/<group_id>")
def get_jargon_group(group_id: str):
    """
    Jargon group endpoint
    ---
    get:
      description: Get a jargon group from the database
      parameters:
        - name: group_id
          in: path
          description: Jargon group identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: Jargon group JSON record
          content:
            application/json:
              schema: JargonGroupSchema
    """

    controller = JargonGroupController(g.session)

    group = controller.get(group_id)
    schema = JargonGroupSchema()
    record = schema.dump(group)

    return jsonify(record), 200
