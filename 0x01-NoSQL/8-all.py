#!/usr/bin/env python3
"""
script to gets all docs in a collection
"""
from typing import List, Any
from pymongo.cursor import Cursor
from pymongo.collection import Collection


def list_all(mongo_collection: Collection[Any]) -> Cursor[Any]:
    """lists all documents in a collection"""
    return mongo_collection.find()
