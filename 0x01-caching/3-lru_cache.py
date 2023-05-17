#!/usr/bin/env python3
"""
3-LRU_Cache Module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """Child of BaseCaching defines:
    - put method for adding items to cache
    - get method for retrieving items from cache
    """

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.item_order = OrderedDict()

    def put(self, key, item):
        """Adds item to cache"""
        if key and item:
            self.item_order[key] = item
            self.item_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.item_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.item_order) > BaseCaching.MAX_ITEMS:
            self.item_order.popitem(last=False)

    def get(self, key):
        """removes item from cache"""
        if key in self.cache_data:
            self.item_order.move_to_end(key)
            return self.cache_data[key]
        return None
