#!/usr/bin/env python3
"""
Module with function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    res = mongo_collection.find({"topics": {"$in": [topic]}})
    return res
