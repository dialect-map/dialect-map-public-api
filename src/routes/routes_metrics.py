# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from globals import service


bp = Blueprint("metrics", __name__)


# ----------- Category Jargon Metrics model ----------- #


@bp.route("/category/metrics/<metric_id>", methods=["GET"])
def get_cat_metrics(metric_id: str):
    """
    Gets a category jargon metric from the underlying database
    :param metric_id: ID of the metric to get
    :return: HTTP 200 response
    """

    record = service.jargon_cat_metrics.get(metric_id)
    return jsonify(record.data), 200


@bp.route("/category/<category_id>/metrics/jargon/<jargon_id>", methods=["GET"])
def get_cat_metrics_by_jargon(jargon_id: str, category_id: str = None):
    """
    Gets a category jargon metric from the underlying database
    :param jargon_id: ID of the jargon to get metrics from
    :param category_id: ID of the category to filter metrics by (optional)
    :return: HTTP 200 response
    """

    records = service.jargon_cat_metrics.get_by_jargon(jargon_id, category_id)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


# ------------ Paper Jargon Metrics model ------------ #


@bp.route("/paper/metrics/<metric_id>", methods=["GET"])
def get_paper_metrics(metric_id: str):
    """
    Gets a paper jargon metric from the underlying database
    :param metric_id: ID of the metric to get
    :return: HTTP 200 response
    """

    record = service.jargon_paper_metrics.get(metric_id)
    return jsonify(record.data), 200


@bp.route("/paper/<path:paper_id>/rev/<paper_rev>/metrics/jargon/<jargon_id>", methods=["GET"])
def get_paper_metrics_by_jargon(jargon_id: str, paper_id: str = None, paper_rev: int = None):
    """
    Gets a paper jargon metric from the underlying database
    :param jargon_id: ID of the jargon to get metrics from
    :param paper_id: ID of the paper to filter metrics by (optional)
    :param paper_rev: revision of the paper to filter metrics by (optional)
    :return: HTTP 200 response
    """

    records = service.jargon_paper_metrics.get_by_jargon(jargon_id, paper_id, paper_rev)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200


@bp.route("/paper/metrics/latest/<jargon_id>", methods=["GET"])
def get_latest_paper_metrics(jargon_id: str):
    """
    Gets latest paper metric records by jargon ID
    :param jargon_id: ID of the metrics associated jargon
    :return: HTTP 200 response
    """

    records = service.jargon_paper_metrics.get_latest_by_jargon(jargon_id)
    records_data = [record.data for record in records]
    return jsonify(records_data), 200
