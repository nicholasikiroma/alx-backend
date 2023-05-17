#!/usr/bin/env python3
"""
0-FIFO_Cache Module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Child of BaseCaching defines:
    - put method for adding items to cache
    - get method for retrieving items from cache
    - No limit is set to Caching System
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item

        if len(self.cache_data) >= self.MAX_ITEMS \
                and key not in self.cache_data:
            last_key = self.queue.pop(-1)
            self.cache_data.pop(last_key)
            print("DISCARD:", last_key)

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
