# -*- coding: utf-8 -*-

from globals import service


def clean_session(error: Exception) -> None:
    """
    Request teardown handler for cleaning sessions.
    This is particularly relevant when using 'scoped-sessions'
    Ref: https://docs.sqlalchemy.org/en/14/orm/contextual.html
    :param error: exception to be dealt with (optional)
    """

    service.db.close_session()
