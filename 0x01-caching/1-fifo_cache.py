#!/usr/bin/python3
""" BaseCaching Module """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and implements a
    caching system using FIFO algorithm
    """

    def __init__(self):
        """ Initialize the FIFO cache
        """
        super().__init__()
        self.cache_queue = []  # Maintains the order of insertion (FIFO)

    def put(self, key, item):
        """ Add an item to the cache using FIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Evict the first item inserted (FIFO)
                oldest_key = self.cache_queue.pop(0)
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))

            self.cache_data[key] = item
            self.cache_queue.append(key)

    def get(self, key):
        """ Get an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
