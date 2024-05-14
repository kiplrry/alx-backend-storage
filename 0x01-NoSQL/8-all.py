#!/usr/bin/env python3
"""
script to gets all docs in a collection
"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    return mongo_collection.find()
