# -*- coding: utf-8 -*-

from flask import Response
from flask import g

from ..globals import database


def create_session() -> None:
    """
    Request setup handler for creating sessions
    """

    g.session = database.create_session()


def remove_session(resp: Response) -> Response:
    """
    Request teardown handler for closing sessions.
    :param resp: request response
    """

    g.session.close()

    return resp
