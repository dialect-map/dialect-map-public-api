# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import request
from globals import service

from dialect_map.models import PaperReference


bp = Blueprint("references", __name__)


@bp.route("/reference/<reference_id>", methods=["GET"])
def get_reference(reference_id: str):
    """
    Gets a paper reference from the underlying database
    :param reference_id: ID of the paper reference to get
    :return: HTTP 200 response
    """

    record = service.paper_refs.get(reference_id)
    return jsonify(record.data), 200


@bp.route("/references/source/<paper_id>/<paper_rev>", methods=["GET"])
def get_references_by_source_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper reference from the underlying database
    :param paper_id: ID of the source paper references
    :param paper_rev: revision of the source paper references
    :return: HTTP 200 response
    """

    records = service.paper_refs.get_by_source_paper(paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


@bp.route("/references/target/<paper_id>/<paper_rev>", methods=["GET"])
def get_references_by_target_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper reference from the underlying database
    :param paper_id: ID of the target paper references
    :param paper_rev: revision of the target paper references
    :return: HTTP 200 response
    """

    records = service.paper_refs.get_by_target_paper(paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


@bp.route("/reference", methods=["POST"])
def create_reference():
    """
    Creates a paper reference with the provided JSON body
    :return: HTTP 201 response
    """

    json = request.json
    ref = PaperReference(**json)
    resp = service.paper_refs.create(ref)
    return jsonify({"id": resp}), 201


@bp.route("/reference/<reference_id>", methods=["DELETE"])
def delete_reference(reference_id: str):
    """
    Deletes a paper reference from the underlying database
    :param reference_id: ID of the paper reference to delete
    :return: HTTP 200 response
    """

    service.paper_refs.delete(reference_id)
    return jsonify({}), 204
