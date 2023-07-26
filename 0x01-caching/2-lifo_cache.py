#!/usr/bin/python3
""" BaseCaching Module """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and implements a
    caching system using LIFO algorithm
    """

    def __init__(self):
        """ Initialize the LIFO cache
        """
        super().__init__()
        self.cache_stack = []  # Maintains the order of insertion (LIFO)

    def put(self, key, item):
        """ Add an item to the cache using LIFO algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # Evict the last item inserted (LIFO)
                last_key = self.cache_stack.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

            self.cache_data[key] = item
            self.cache_stack.append(key)

    def get(self, key):
        """ Get an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
