# -*- coding: utf-8 -*-

import logging
from flask import jsonify
from flask import Response
from typing import Tuple

logger = logging.getLogger()


def error_handler(error: Exception, code: int) -> Tuple[Response, int]:
    """
    Generic exception handler function to be used in a web application
    :param error: exception to be dealt with
    :param code: HTTP status code to return
    :return: (JSON, HTTP status code)
    """

    error_type = error.__class__
    error_msg = str(error)

    logger.error(f"Exception {error_type}: {error_msg}")
    return jsonify({"message": error_msg}), code
