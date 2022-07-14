# -*- coding: utf-8 -*-

from flask import Response
from flask import current_app
from flask import g


def create_session() -> None:
    """
    Request setup handler for creating sessions
    """

    database = current_app.extensions["database"]
    session = database.create_session()

    g.session = session


def remove_session(resp: Response) -> Response:
    """
    Request teardown handler for closing sessions.
    :param resp: request response
    """

    g.session.close()

    return resp
