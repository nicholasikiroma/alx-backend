#!/usr/bin/env python3
"""Module implements a simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Returns tuple"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
