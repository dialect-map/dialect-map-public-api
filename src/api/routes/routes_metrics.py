# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify

from dialect_map_schemas import JargonCategoryMetricsSchema
from dialect_map_schemas import JargonPaperMetricsSchema

from ..globals import service


bp = Blueprint("metrics", __name__)


# ----------- Category Jargon Metrics model ----------- #


@bp.get("/category-metrics/<metric_id>")
def get_cat_metrics(metric_id: str):
    """
    ArXiv category metrics endpoint
    ---
    get:
      description: Get a set of ArXiv category metrics from the database
      parameters:
        - name: metric_id
          in: path
          description: ArXiv category metrics identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: ArXiv category metrics JSON record
          content:
            application/json:
              schema: JargonCategoryMetricsSchema
    """

    metric = service.jargon_cat_metrics.get(metric_id)
    schema = JargonCategoryMetricsSchema()
    record = schema.dump(metric)

    return jsonify(record), 200


@bp.get("/category-metrics/jargon/<jargon_id>")
@bp.get("/category-metrics/jargon/<jargon_id>/<category_id>")
def get_category_metrics_by_jargon(jargon_id: str, category_id: str = None):
    """
    ArXiv category metrics by jargon endpoint
    ---
    get:
      description: Get a list of ArXiv category metrics from the database
      parameters:
        - name: jargon_id
          in: path
          description: Jargon term identifier
          required: true
          schema:
            type: string
        - name: category_id
          in: path
          description: ArXiv category identifier
          required: false
          schema:
            type: string
      responses:
        200:
          description: ArXiv category metrics JSON records
          content:
            application/json:
              schema:
                type: array
                items: JargonCategoryMetricsSchema
    """

    metrics = service.jargon_cat_metrics.get_by_jargon(jargon_id, category_id)
    schemas = JargonCategoryMetricsSchema(many=True)
    records = schemas.dump(metrics)

    return jsonify(records), 200


# ------------ Paper Jargon Metrics model ------------ #


@bp.get("/paper-metrics/<metric_id>")
def get_paper_metrics(metric_id: str):
    """
    ArXiv paper metrics endpoint
    ---
    get:
      description: Get a set of ArXiv paper metrics from the database
      parameters:
        - name: metric_id
          in: path
          description: ArXiv paper metrics identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: ArXiv paper metrics JSON record
          content:
            application/json:
              schema: JargonPaperMetricsSchema
    """

    metric = service.jargon_paper_metrics.get(metric_id)
    schema = JargonPaperMetricsSchema()
    record = schema.dump(metric)

    return jsonify(record), 200


@bp.get("/paper-metrics/jargon/<jargon_id>")
@bp.get("/paper-metrics/jargon/<jargon_id>/<path:paper_id>")
@bp.get("/paper-metrics/jargon/<jargon_id>/<path:paper_id>/rev/<int:paper_rev>")
def get_paper_metrics_by_jargon(jargon_id: str, paper_id: str = None, paper_rev: int = None):
    """
    ArXiv paper metrics by jargon endpoint
    ---
    get:
      description: Get a list of ArXiv paper metrics from the database
      parameters:
        - name: jargon_id
          in: path
          description: Jargon term identifier
          required: true
          schema:
            type: string
        - name: paper_id
          in: path
          description: ArXiv paper identifier
          required: false
          schema:
            type: string
        - name: paper_rev
          in: path
          description: ArXiv paper revision
          required: false
          schema:
            type: integer
      responses:
        200:
          description: ArXiv paper metrics JSON records
          content:
            application/json:
              schema:
                type: array
                items: JargonPaperMetricsSchema
    """

    metrics = service.jargon_paper_metrics.get_by_jargon(jargon_id, paper_id, paper_rev)
    schemas = JargonPaperMetricsSchema(many=True)
    records = schemas.dump(metrics)

    return jsonify(records), 200


@bp.get("/paper-metrics/jargon/<jargon_id>/latest")
def get_latest_paper_metrics(jargon_id: str):
    """
    ArXiv papers latest metrics by jargon endpoint
    ---
    get:
      description: Get a list of ArXiv paper metrics from the database
      parameters:
        - name: jargon_id
          in: path
          description: Jargon term identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: ArXiv paper latest metrics JSON records
          content:
            application/json:
              schema:
                type: array
                items: JargonPaperMetricsSchema
    """

    metrics = service.jargon_paper_metrics.get_latest_by_jargon(jargon_id)
    schemas = JargonPaperMetricsSchema(many=True)
    records = schemas.dump(metrics)

    return jsonify(records), 200
