# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

from dialect_map_schemas import PaperSchema
from dialect_map_schemas import PaperAuthorSchema
from dialect_map_schemas import PaperReferenceCountersSchema

from ..globals import service


bp = Blueprint("papers", __name__)


# --------------------- Paper model --------------------- #


@bp.get("/paper/<path:paper_id>/rev/<paper_rev>")
def get_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper from the underlying database
    :param paper_id: ID of the paper to get
    :param paper_rev: revision of the paper to get
    :return: HTTP 200 response
    """

    paper = service.papers.get(paper_id, paper_rev)
    schema = PaperSchema()
    record = schema.dump(paper)

    return jsonify(record), 200


# ------------------ Paper Author model ------------------ #


@bp.get("/paper/author/<author_id>")
def get_paper_author(author_id: str):
    """
    Gets a paper author from the underlying database
    :param author_id: ID of the paper author to get
    :return: HTTP 200 response
    """

    author = service.paper_authors.get(author_id)
    schema = PaperAuthorSchema()
    record = schema.dump(author)

    return jsonify(record), 200


@bp.get("/paper/<path:paper_id>/rev/<paper_rev>/authors")
def get_paper_authors_by_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper authors from the underlying database
    :param paper_id: ID of the paper to get the authors from
    :param paper_rev: revision of the paper to get the authors from
    :return: HTTP 200 response
    """

    authors = service.paper_authors.get_by_paper(paper_id, paper_rev)
    schemas = PaperAuthorSchema(many=True)
    records = schemas.dump(authors)

    return jsonify(records), 200


# --------------- Paper Ref Counters model --------------- #


@bp.get("/paper/reference/counters/<counter_id>")
def get_ref_counter(counter_id: str):
    """
    Gets a paper ref. counter from the underlying database
    :param counter_id: ID of the paper ref. counter to get
    :return: HTTP 200 response
    """

    counter = service.paper_ref_counters.get(counter_id)
    schema = PaperReferenceCountersSchema()
    record = schema.dump(counter)

    return jsonify(record), 200


@bp.get("/paper/<path:paper_id>/rev/<paper_rev>/reference/counters")
def get_ref_counter_by_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper ref. counter from the underlying database
    :param paper_id: ID of the paper to get the ref. counter from
    :param paper_rev: revision of the paper to get the ref. counter from
    :return: HTTP 200 response
    """

    counters = service.paper_ref_counters.get_by_paper(paper_id, paper_rev)
    schemas = PaperReferenceCountersSchema(many=True)
    records = schemas.dump(counters)

    return jsonify(records), 200
