#!/usr/bin/env python3
"""Task 2: Hypermedia pagination"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """Returns start and end index of page"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns requested page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        index = index_range(page, page_size)
        data = self.dataset()

        page = [line for line in data[index[0]: index[1]]]
        return page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Creates hyper pagination"""
        data = self.get_page(page, page_size)
        size = len(data)
        total = math.ceil((len(self.dataset()) / page_size))
        next = page + 1
        if next > total:
            next = None
        prev = page - 1
        if prev == 0:
            prev = None

        return {
            "page_size": size,
            "page": page,
            "data": data,
            "next_page": next,
            "prev_page": prev,
            "total pages": total,
        }
