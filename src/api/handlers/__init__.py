# -*- coding: utf-8 -*-

from json import JSONDecodeError

from .context import create_session
from .context import remove_session
from .errors import *


error_mappings = [
    ErrorMapping(request_error_handler, [JSONDecodeError]),
    ErrorMapping(not_found_error_handler, [ValueError]),
    ErrorMapping(unknown_error_handler, [Exception]),
]
