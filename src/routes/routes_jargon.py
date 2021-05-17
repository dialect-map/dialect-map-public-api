# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import request
from globals import service
from urllib import parse


bp = Blueprint("jargons", __name__)


# ------------------- Jargon model ------------------- #


@bp.get("/jargon/<jargon_id>")
def get_jargon(jargon_id: str):
    """
    Gets a jargon from the underlying database
    :param jargon_id: ID of the jargon to get
    :return: HTTP 200 response
    """

    record = service.jargons.get(jargon_id)
    return jsonify(record.data), 200


@bp.get("/jargon/all")
def get_jargon_all():
    """
    Gets all jargons from the underlying database
    :return: HTTP 200 response
    """

    include_archived = request.args.get(
        key="archived",
        type=bool,
        default=False,
    )

    records = service.jargons.get_all(include_archived)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


@bp.get("/jargon/string/<jargon_str>")
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


@bp.get("/jargon/group/<group_id>")
def get_jargon_by_group(group_id: str):
    """
    Gets a list of jargons from the underlying database
    :param group_id: group ID to filter the jargons by
    :return: HTTP 200 response
    """

    records = service.jargons.get_by_group(group_id)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


# ---------------- Jargon Group model ---------------- #


@bp.get("/jargon-group/<group_id>")
def get_jargon_group(group_id: str):
    """
    Gets a jargon group from the underlying database
    :param group_id: ID of the jargon group to get
    :return: HTTP 200 response
    """

    record = service.jargon_groups.get(group_id)
    return jsonify(record.data), 200
