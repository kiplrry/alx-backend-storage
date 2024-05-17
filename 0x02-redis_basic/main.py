#!/usr/bin/env python3
""" Main file """
from redis import Redis
from web import get_page

url = 'http://slowwly.robertomurray.co.uk'

get_page(url)

r = Redis()

j = r.get(url)
print(j)
count = r.get(f'counts:{url}')
print(count)