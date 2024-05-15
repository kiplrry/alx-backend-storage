#!/usr/bin/env python3
"""
module implementing the cache class
"""

import redis
from typing import Union
from uuid import uuid4


class Cache():
    """Cache class"""

    def __init__(self) -> None:
        """initiates the class with a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a data with a random key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

# class Cache:
#     """Create a Cache class"""

#     def __init__(self):
#         """store an instance of the Redis client"""
#         self._redis = redis.Redis()
#         self._redis.flushdb()


#     def store(self, data: Union[str, bytes, int, float]) -> str:
#         """generate a random key"""
#         random_key = str(uuid4())
#         self._redis.set(random_key, data)
#         return random_key
