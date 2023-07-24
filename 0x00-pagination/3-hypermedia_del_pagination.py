#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Ftn that returns a dict with updated k, v pairs"""
        # Verify that the index argument is within a valid range
        assert (isinstance(index, int)
                                 and index >= 0), "Invalid index value."
        assert 0 <= index < len(self.indexed_dataset())
        assert isinstance(page_size, int) and page_size > 0

        # Get the dataset length and calculate total pages
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # Calculate the current start index of the return page
        # (index of the first item)
        if index is None:
            index = 0
        else:
            index = min(index, total_items - 1)

        # Get the actual page of the dataset
        paginated_data = self.dataset()[index:index + page_size]

        # Calculate the next index to query with (index of the first
        # item after the last item on the current page)
        next_index = min(index + page_size, total_items)

        # Create the dictionary with the required key-value pairs
        hyper_data = {
            "index": index,
            "next_index": next_index,
            "page_size": len(paginated_data),
            "data": paginated_data
        }

        return hyper_data
