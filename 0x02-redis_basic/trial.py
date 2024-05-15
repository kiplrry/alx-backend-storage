#!/usr/bin/python3

import redis

r = redis.Redis(decode_responses=True)
r.set('juno', '23')
print(type(r.get('juno')))