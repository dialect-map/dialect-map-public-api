# -*- coding: utf-8 -*-

import json

from .context import create_session
from .context import remove_session
from .errors import *


error_mappings = [
    {"handler": request_error_handler, "errors": [json.JSONDecodeError]},
    {"handler": not_found_error_handler, "errors": [ValueError]},
    {"handler": unknown_error_handler, "errors": [Exception]},
]
