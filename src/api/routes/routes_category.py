# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import jsonify
from flask import request

from dialect_map_schemas import CategorySchema

from ..globals import service


bp = Blueprint("categories", __name__)


@bp.get("/category/<category_id>")
def get_category(category_id: str):
    """
    ArXiv category endpoint
    ---
    get:
      description: Get an ArXiv category from the database
      parameters:
        - name: category_id
          in: path
          description: ArXiv category identifier
          required: true
          schema:
            type: string
      responses:
        200:
          description: ArXiv category JSON record
          content:
            application/json:
              schema: CategorySchema
    """

    category = service.categories.get(category_id)
    schema = CategorySchema()
    record = schema.dump(category)

    return jsonify(record), 200


@bp.get("/category/all")
def get_category_all():
    """
    All ArXiv categories endpoint
    ---
    get:
      description: Get all ArXiv categories from the database
      parameters:
        - name: archived
          in: query
          description: Flag to whether or not include archived categories
          required: false
          schema:
            type: boolean
      responses:
        200:
          description: ArXiv category JSON records
          content:
            application/json:
              schema:
                type: array
                items: CategorySchema
    """

    include_archived = request.args.get(
        key="archived",
        type=bool,
        default=False,
    )

    categories = service.categories.get_all(include_archived)
    schemas = CategorySchema(many=True)
    records = schemas.dump(categories)

    return jsonify(records), 200
