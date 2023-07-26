#!/usr/bin/python3
""" BaseCaching Module """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements
    a caching system using LRU algorithm
    """

    def __init__(self):
        """ Initialize the LRU cache
        """
        super().__init__()
        self.cache_queue = []  # Maintains the order of recently accessed keys

    def put(self, key, item):
        """ Add an item to the cache using LRU algorithm
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If the key exists, update its value
                self.cache_data[key] = item
                # Move accessed key to end of queue (most recently used)
                self.cache_queue.remove(key)
                self.cache_queue.append(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Evict the least recently used item (LRU)
                    lru_key = self.cache_queue.pop(0)
                    del self.cache_data[lru_key]
                    print("DISCARD: {}".format(lru_key))

                self.cache_data[key] = item
                self.cache_queue.append(key)

    def get(self, key):
        """ Get an item from the cache using LRU algorithm
        """
        if key is not None and key in self.cache_data:
            # Move accessed key to end of queue (most recently used)
            self.cache_queue.remove(key)
            self.cache_queue.append(key)
            return self.cache_data[key]
        else:
            return None
