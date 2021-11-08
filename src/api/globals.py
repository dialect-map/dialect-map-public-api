# -*- coding: utf-8 -*-

import atexit

from dialect_map.service import ApplicationService
from dialect_map.storage import SQLAlchemyDatabase

from .config import ApplicationConfig


service: ApplicationService


def setup_service(c: ApplicationConfig):
    """
    Setup the global application service
    :param c: global application configuration
    """

    global service

    engine = SQLAlchemyDatabase(c.database_url)
    service = ApplicationService(engine)

    # Register the service cleanup function upon exiting
    atexit.register(service.stop)
