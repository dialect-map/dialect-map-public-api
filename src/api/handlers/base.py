# -*- coding: utf-8 -*-

import logging

from typing import Tuple

from flask import jsonify
from flask import Response


logger = logging.getLogger()


def error_handler(error: Exception, code: int) -> Tuple[Response, int]:
    """
    Generic exception handler function to be used in a web application
    :param error: exception to be dealt with
    :param code: HTTP status code to return
    :return: (JSON, HTTP status code)
    """

    ### NOTE:
    ### Unwraps the original error if it exists (SQLAlchemy specific)
    error = getattr(error, "orig", error)

    error_type = str(error.__class__.__name__)
    error_msg = str(error)

    logger.error(f"Exception {error_type}: {error_msg}")
    return jsonify({"message": error_msg}), code
