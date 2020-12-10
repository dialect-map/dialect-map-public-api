# -*- coding: utf-8 -*-

from functools import partial

from .base import error_handler


# Error handler returning HTTP code 400
request_error_handler = partial(error_handler, code=400)

# Error handler returning HTTP code 404
not_found_error_handler = partial(error_handler, code=404)

# Error handler returning HTTP code 500
unknown_error_handler = partial(error_handler, code=500)
