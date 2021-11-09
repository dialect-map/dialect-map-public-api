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
    Gets a category jargon metric from the underlying database
    :param metric_id: ID of the metric to get
    :return: HTTP 200 response
    """

    metric = service.jargon_cat_metrics.get(metric_id)
    schema = JargonCategoryMetricsSchema()
    record = schema.dump(metric)

    return jsonify(record), 200


@bp.get("/category-metrics/jargon/<jargon_id>")
@bp.get("/category-metrics/jargon/<jargon_id>/<category_id>")
def get_category_metrics_by_jargon(jargon_id: str, category_id: str = None):
    """
    Gets a category jargon metric from the underlying database
    :param jargon_id: ID of the jargon to get metrics from
    :param category_id: ID of the category to filter metrics by (optional)
    :return: HTTP 200 response
    """

    metrics = service.jargon_cat_metrics.get_by_jargon(jargon_id, category_id)
    schemas = JargonCategoryMetricsSchema(many=True)
    records = schemas.dump(metrics)

    return jsonify(records), 200


# ------------ Paper Jargon Metrics model ------------ #


@bp.get("/paper-metrics/<metric_id>")
def get_paper_metrics(metric_id: str):
    """
    Gets a paper jargon metric from the underlying database
    :param metric_id: ID of the metric to get
    :return: HTTP 200 response
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
    Gets a paper jargon metric from the underlying database
    :param jargon_id: ID of the jargon to get metrics from
    :param paper_id: ID of the paper to filter metrics by (optional)
    :param paper_rev: revision of the paper to filter metrics by (optional)
    :return: HTTP 200 response
    """

    metrics = service.jargon_paper_metrics.get_by_jargon(jargon_id, paper_id, paper_rev)
    schemas = JargonPaperMetricsSchema(many=True)
    records = schemas.dump(metrics)

    return jsonify(records), 200


@bp.get("/paper-metrics/jargon/<jargon_id>/latest")
def get_latest_paper_metrics(jargon_id: str):
    """
    Gets latest paper metric records by jargon ID
    :param jargon_id: ID of the metrics associated jargon
    :return: HTTP 200 response
    """

    metrics = service.jargon_paper_metrics.get_latest_by_jargon(jargon_id)
    schemas = JargonPaperMetricsSchema(many=True)
    records = schemas.dump(metrics)

    return jsonify(records), 200
