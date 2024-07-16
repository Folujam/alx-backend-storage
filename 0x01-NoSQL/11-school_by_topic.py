#!/usr/bin/env python3
"""Mongodb Module."""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]

if __name__ == "__main__":
    """the main execusioner"""
    schools_by_topic(mongo_collection, topic)
