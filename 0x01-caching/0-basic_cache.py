#!/usr/bin/env python3
"""
0-Basic_Cache Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Child of BaseCaching defines:
    - put method for adding items to cache
    - get method for retrieving items from cache
    - No limit is set to Caching System
    """

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
