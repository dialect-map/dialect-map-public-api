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
    ArXiv paper endpoint
    ---
    get:
      description: Get an ArXiv paper from the database
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
          description: ArXiv paper JSON record
          content:
            application/json:
              schema: PaperSchema
    """

    paper = service.papers.get(paper_id, paper_rev)
    schema = PaperSchema()
    record = schema.dump(paper)

    return jsonify(record), 200


# ------------------ Paper Author model ------------------ #


@bp.get("/paper/author/<author_id>")
def get_paper_author(author_id: str):
    """
    ArXiv paper author endpoint
    ---
    get:
      description: Get an ArXiv paper author from the database
      parameters:
        - name: author_id
          in: path
          description: ArXiv paper author identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: ArXiv paper author JSON record
          content:
            application/json:
              schema: PaperAuthorSchema
    """

    author = service.paper_authors.get(author_id)
    schema = PaperAuthorSchema()
    record = schema.dump(author)

    return jsonify(record), 200


@bp.get("/paper/<path:paper_id>/rev/<paper_rev>/authors")
def get_paper_authors_by_paper(paper_id: str, paper_rev: int):
    """
    ArXiv paper author by paper endpoint
    ---
    get:
      description: Get a list of ArXiv paper authors from the database
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
          description: ArXiv paper author JSON records
          content:
            application/json:
              schema:
                type: array
                items: PaperAuthorSchema
    """

    authors = service.paper_authors.get_by_paper(paper_id, paper_rev)
    schemas = PaperAuthorSchema(many=True)
    records = schemas.dump(authors)

    return jsonify(records), 200


# --------------- Paper Ref Counters model --------------- #


@bp.get("/paper/reference/counters/<counter_id>")
def get_ref_counter(counter_id: str):
    """
    ArXiv paper reference counters endpoint
    ---
    get:
      description: Get a set of ArXiv paper reference counters from the database
      parameters:
        - name: counter_id
          in: path
          description: ArXiv paper reference counters identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: ArXiv paper reference counters JSON record
          content:
            application/json:
              schema: PaperReferenceCountersSchema
    """

    counter = service.paper_ref_counters.get(counter_id)
    schema = PaperReferenceCountersSchema()
    record = schema.dump(counter)

    return jsonify(record), 200


@bp.get("/paper/<path:paper_id>/rev/<paper_rev>/reference/counters")
def get_ref_counter_by_paper(paper_id: str, paper_rev: int):
    """
    ArXiv paper reference counters by paper endpoint
    ---
    get:
      description: Get a list of ArXiv paper reference counters from the database
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
          description: ArXiv paper reference counters JSON records
          content:
            application/json:
              schema:
                type: array
                items: PaperReferenceCountersSchema
    """

    counters = service.paper_ref_counters.get_by_paper(paper_id, paper_rev)
    schemas = PaperReferenceCountersSchema(many=True)
    records = schemas.dump(counters)

    return jsonify(records), 200
