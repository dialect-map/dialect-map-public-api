# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from globals import service


bp = Blueprint("papers", __name__)


# --------------------- Paper model --------------------- #


@bp.route("/paper/<path:paper_id>/rev/<paper_rev>", methods=["GET"])
def get_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper from the underlying database
    :param paper_id: ID of the paper to get
    :param paper_rev: revision of the paper to get
    :return: HTTP 200 response
    """

    record = service.papers.get(paper_id, paper_rev)
    return jsonify(record.data), 200


# ------------------ Paper Author model ------------------ #


@bp.route("/paper/author/<author_id>", methods=["GET"])
def get_paper_author(author_id: str):
    """
    Gets a paper author from the underlying database
    :param author_id: ID of the paper author to get
    :return: HTTP 200 response
    """

    record = service.paper_authors.get(author_id)
    return jsonify(record.data), 200


@bp.route("/paper/<path:paper_id>/rev/<paper_rev>/authors", methods=["GET"])
def get_paper_authors_by_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper authors from the underlying database
    :param paper_id: ID of the paper to get the authors from
    :param paper_rev: revision of the paper to get the authors from
    :return: HTTP 200 response
    """

    records = service.paper_authors.get_by_paper(paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


# --------------- Paper Ref Counters model --------------- #


@bp.route("/paper/reference/counters/<counter_id>", methods=["GET"])
def get_ref_counter(counter_id: str):
    """
    Gets a paper ref. counter from the underlying database
    :param counter_id: ID of the paper ref. counter to get
    :return: HTTP 200 response
    """

    record = service.paper_ref_counters.get(counter_id)
    return jsonify(record.data), 200


@bp.route("/paper/<path:paper_id>/rev/<paper_rev>/reference/counters", methods=["GET"])
def get_ref_counter_by_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper ref. counter from the underlying database
    :param paper_id: ID of the paper to get the ref. counter from
    :param paper_rev: revision of the paper to get the ref. counter from
    :return: HTTP 200 response
    """

    records = service.paper_ref_counters.get_by_paper(paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200
