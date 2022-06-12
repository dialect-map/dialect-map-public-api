# -*- coding: utf-8 -*-

import atexit

from dialect_map_core.storage import SQLDatabase


database: SQLDatabase = ...


def setup_database(connection_url: str):
    """
    Setup the global application database
    :param connection_url: database connection URL
    """

    global database

    database = SQLDatabase(connection_url)

    # Register the service cleanup function upon exiting
    atexit.register(database.close_connection)
