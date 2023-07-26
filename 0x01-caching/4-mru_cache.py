#!/usr/bin/python3
""" BaseCaching Module """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements
    a caching system using MRU algorithm
    """

    def __init__(self):
        """ Initialize the MRU cache
        """
        super().__init__()
        self.cache_queue = []  # Maintains the order of recently accessed keys

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # Evict the most recently used item (MRU)
                mru_key = self.cache_queue.pop()
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))

            self.cache_data[key] = item
            self.cache_queue.append(key)

    def get(self, key):
        """ Get an item from the cache using MRU algorithm
        """
        if key is not None and key in self.cache_data:
            # Move accessed key to end of queue (most recently used)
            self.cache_queue.remove(key)
            self.cache_queue.append(key)
            return self.cache_data[key]
        else:
            return None
