#!/usr/bin/env python3
"""module implementing the cache class"""

from redis import Redis
from typing import Union
from uuid import uuid4


class Cache():
    """Cache class"""
    def __init__(self) -> None:
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, float, int, bytes]) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key
