# -*- coding: utf-8 -*-

from urllib import parse

from flask import Blueprint
from flask import jsonify
from flask import request

from dialect_map_schemas import JargonSchema
from dialect_map_schemas import JargonGroupSchema

from ..globals import service


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

    jargon = service.jargons.get(jargon_id)
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

    jargons = service.jargons.get_all(include_archived)
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

    string = parse.unquote(jargon_str)
    string = string.lower()

    jargon = service.jargons.get_by_string(string)

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

    jargons = service.jargons.get_by_group(group_id)
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

    group = service.jargon_groups.get(group_id)
    schema = JargonGroupSchema()
    record = schema.dump(group)

    return jsonify(record), 200
