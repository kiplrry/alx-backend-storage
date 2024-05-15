#!/usr/bin/env python3
"""module implementing the cache class"""

import redis
from typing import Union
from uuid import uuid4


class Cache():
    """Cache class"""
    def __init__(self):
        """initiates the class with a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        """Stores a data with a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
