# -*- coding: utf-8 -*-

from typing import Optional


def build_paper_id(paper_id: str, category: Optional[str]) -> str:
    """
    Builds a paper ID independently of the ArXiv submission date.
    Papers submitted before April 2007 get their main category as ID prefix.
    :param paper_id: provided paper ID
    :param category: provided paper category (if any)
    :return: valid ID
    """

    if category:
        return f"{category}/{paper_id}"
    else:
        return f"{paper_id}"
