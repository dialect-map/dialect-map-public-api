# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

from dialect_map_schemas import PaperReferenceSchema

from ..globals import service


bp = Blueprint("references", __name__)


@bp.get("/reference/<reference_id>")
def get_reference(reference_id: str):
    """
    ArXiv reference endpoint
    ---
    get:
      description: Get an ArXiv reference from the database
      parameters:
        - name: reference_id
          in: path
          description: ArXiv reference identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: ArXiv reference JSON record
          content:
            application/json:
              schema: PaperReferenceSchema
    """

    ref = service.paper_refs.get(reference_id)
    schema = PaperReferenceSchema()
    record = schema.dump(ref)

    return jsonify(record), 200


@bp.get("/references/source/<path:paper_id>/rev/<paper_rev>")
def get_references_by_source_paper(paper_id: str, paper_rev: int):
    """
    ArXiv reference by source paper endpoint
    ---
    get:
      description: Get a list of ArXiv references from the database
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
          description: ArXiv reference JSON records
          content:
            application/json:
              schema:
                type: array
                items: PaperReferenceSchema
    """

    refs = service.paper_refs.get_by_source_paper(paper_id, paper_rev)
    schemas = PaperReferenceSchema(many=True)
    records = schemas.dump(refs)

    return jsonify(records), 200


@bp.get("/references/target/<path:paper_id>/rev/<paper_rev>")
def get_references_by_target_paper(paper_id: str, paper_rev: int):
    """
    ArXiv reference by target paper endpoint
    ---
    get:
      description: Get a list of ArXiv references from the database
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
          description: ArXiv reference JSON records
          content:
            application/json:
              schema:
                type: array
                items: PaperReferenceSchema
    """

    refs = service.paper_refs.get_by_target_paper(paper_id, paper_rev)
    schemas = PaperReferenceSchema(many=True)
    records = schemas.dump(refs)

    return jsonify(records), 200
