#!/usr/bin/env python3
"""
module implementing the cache class
"""

import redis
from typing import Union, Callable, Optional
from uuid import uuid4
from functools import wraps


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        inputs = str(args)
        self._redis.rpush(f'{key}:inputs', inputs)
        out = method(self, *args, **kwargs)
        self._redis.rpush(f'{key}:outputs', out)
        return out
    return wrapper


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """Cache class"""

    def __init__(self) -> None:
        """initiates the class with a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
