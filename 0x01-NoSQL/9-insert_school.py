#!/usr/bin/env python3
"""Insert with python Module"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new doc in a collectn, returns new id"""
    id = mongo_collection.insert(kwargs)
    return id.inserted_id

if __name__ == "__main__":
    """the main execusioner"""
    insert_school(mongo_collection, kwargs)
