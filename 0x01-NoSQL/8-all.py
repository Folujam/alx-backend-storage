#!/usr/bin/env python3
"""Py MongoDB Module"""


def list_all(mongo_collection):
    """lists all documents in collection"""
    return [document for document in mongo_collection.find()]

if __name__ == "__main__":
    """this is execusioner"""
    list_all(mongo_collection)
