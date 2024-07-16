#!/usr/bin/env python3
"""Update Module"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a schoool document"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

if __name__ == "__main__":
    """the main execusioner"""
    update_topics(mongo_collection, name, topics)
