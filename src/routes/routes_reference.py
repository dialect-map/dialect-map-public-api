# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from globals import service

from .__utils import build_paper_id


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
@bp.route("/references/source/<category>/<paper_id>/<paper_rev>", methods=["GET"])
def get_references_by_source_paper(paper_id: str, paper_rev: int, category: str = None):
    """
    Gets a paper reference from the underlying database
    :param paper_id: ID of the source paper references
    :param paper_rev: revision of the source paper references
    :param category: name of the paper main category (optional)
    :return: HTTP 200 response
    """

    # Builds a valid paper ID
    paper_id = build_paper_id(paper_id, category)

    records = service.paper_refs.get_by_source_paper(paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


@bp.route("/references/target/<paper_id>/<paper_rev>", methods=["GET"])
@bp.route("/references/target/<category>/<paper_id>/<paper_rev>", methods=["GET"])
def get_references_by_target_paper(paper_id: str, paper_rev: int, category: str = None):
    """
    Gets a paper reference from the underlying database
    :param paper_id: ID of the target paper references
    :param paper_rev: revision of the target paper references
    :param category: name of the paper main category (optional)
    :return: HTTP 200 response
    """

    # Builds a valid paper ID
    paper_id = build_paper_id(paper_id, category)

    records = service.paper_refs.get_by_target_paper(paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200
