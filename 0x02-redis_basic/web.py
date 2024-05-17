#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

import redis
import requests
from typing import Callable
from functools import wraps


def counter(method: Callable) -> Callable:
    r = redis.Redis()

    @wraps(method)
    def wrapper(url):
        r.incr(f'counts:{url}')
        res = r.get(url)
        if not res:
            res = method(url)
            r.set(url, res, 10)
        return res
    return wrapper


@counter
def get_page(url: str) -> str:
    """func to make request to a url"""
    res = requests.get(url).text
    return res
