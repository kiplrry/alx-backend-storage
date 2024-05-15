#!/usr/bin/env python3
"""
module implementing the cache class
"""

import redis
from typing import Union, Callable, Optional
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_int(self, val: str) -> int:
        """returns an int from key"""
        value = self._redis.get(val).decode('utf-8')
        try:
            value = int(value)
        except ValueError:
            value = 0
        return value

    def get_str(self, val: str) -> str:
        """returns a str from key"""
        value = self._redis.get(val)
        return value.decode('utf-8')
