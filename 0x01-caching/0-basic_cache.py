#!/usr/bin/python3
""" BaseCaching Module """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache that inherits from
    BaseCaching and is a caching system"""

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
