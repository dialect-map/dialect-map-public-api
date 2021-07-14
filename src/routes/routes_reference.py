# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from globals import service

from dialect_map_schemas import PaperReferenceSchema


bp = Blueprint("references", __name__)


@bp.get("/reference/<reference_id>")
def get_reference(reference_id: str):
    """
    Gets a paper reference from the underlying database
    :param reference_id: ID of the paper reference to get
    :return: HTTP 200 response
    """

    ref = service.paper_refs.get(reference_id)
    schema = PaperReferenceSchema()
    record = schema.dump(ref)

    return jsonify(record), 200


@bp.get("/references/source/<path:paper_id>/rev/<paper_rev>")
def get_references_by_source_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper reference from the underlying database
    :param paper_id: ID of the source paper references
    :param paper_rev: revision of the source paper references
    :return: HTTP 200 response
    """

    refs = service.paper_refs.get_by_source_paper(paper_id, paper_rev)
    schemas = PaperReferenceSchema(many=True)
    records = schemas.dump(refs)

    return jsonify(records), 200


@bp.get("/references/target/<path:paper_id>/rev/<paper_rev>")
def get_references_by_target_paper(paper_id: str, paper_rev: int):
    """
    Gets a paper reference from the underlying database
    :param paper_id: ID of the target paper references
    :param paper_rev: revision of the target paper references
    :return: HTTP 200 response
    """

    refs = service.paper_refs.get_by_target_paper(paper_id, paper_rev)
    schemas = PaperReferenceSchema(many=True)
    records = schemas.dump(refs)

    return jsonify(records), 200
