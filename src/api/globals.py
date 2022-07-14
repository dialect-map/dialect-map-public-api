# -*- coding: utf-8 -*-

from dialect_map_core.storage import SQLDatabase


def create_database(connection_url: str) -> SQLDatabase:
    """
    Creates the global application database instance
    :param connection_url: database connection URL
    :return: database connection instance
    """

    return SQLDatabase(connection_url)
