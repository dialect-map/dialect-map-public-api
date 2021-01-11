# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import request
from globals import service
from urllib import parse

from dialect_map.models import Jargon
from dialect_map.models import JargonGroup


bp = Blueprint("jargons", __name__)


# ------------------- Jargon model ------------------- #


@bp.route("/jargon/<jargon_id>", methods=["GET"])
def get_jargon(jargon_id: str):
    """
    Gets a jargon from the underlying database
    :param jargon_id: ID of the jargon to get
    :return: HTTP 200 response
    """

    record = service.jargons.get(jargon_id)
    return jsonify(record.data), 200


@bp.route("/jargon/string/<jargon_str>", methods=["GET"])
def get_jargon_by_string(jargon_str: str):
    """
    Gets a jargon from the underlying database
    :param jargon_str: jargon string representation
    :return: HTTP 200 / HTTP 404 responses
    """

    string = parse.unquote(jargon_str)
    string = string.lower()
    record = service.jargons.get_by_string(string)

    if record:
        return jsonify(record.data), 200
    else:
        return jsonify({}), 404


@bp.route("/jargon", methods=["POST"])
def create_jargon():
    """
    Creates a jargon with the provided JSON body
    :return: HTTP 201 response
    """

    json = request.json
    jargon = Jargon(**json)
    resp = service.jargons.create(jargon)
    return jsonify({"id": resp}), 201


@bp.route("/jargon/<jargon_id>", methods=["DELETE"])
def delete_jargon(jargon_id: str):
    """
    Deletes a jargon from the underlying database
    :param jargon_id: ID of the jargon to delete
    :return: HTTP 204 response
    """

    service.jargons.delete(jargon_id)
    return jsonify({}), 204


# ---------------- Jargon Group model ---------------- #


@bp.route("/jargon-group/<group_id>", methods=["GET"])
def get_jargon_group(group_id: str):
    """
    Gets a jargon group from the underlying database
    :param group_id: ID of the jargon group to get
    :return: HTTP 200 response
    """

    record = service.jargon_groups.get(group_id)
    return jsonify(record.data), 200


@bp.route("/jargon-group", methods=["POST"])
def create_jargon_group():
    """
    Creates a jargon group with the provided JSON body
    :return: HTTP 201 response
    """

    json = request.json
    group = JargonGroup(**json)
    resp = service.jargon_groups.create(group)
    return jsonify({"id": resp}), 201


@bp.route("/jargon-group/<group_id>", methods=["DELETE"])
def delete_jargon_group(group_id: str):
    """
    Deletes a jargon group from the underlying database
    :param group_id: ID of the jargon group to delete
    :return: HTTP 204 response
    """

    service.jargon_groups.delete(group_id)
    return jsonify({}), 204
