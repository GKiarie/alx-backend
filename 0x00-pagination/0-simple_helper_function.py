#!/usr/bin/env python3
"""
function named index_range that takes two integer
arguments page and page_size
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    ftn takes in two ints and returns atuple
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return (start_index, end_index)
