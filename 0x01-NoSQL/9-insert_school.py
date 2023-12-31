#!/usr/bin/env python3
""" Contains Python function that inserts a document into a collection"""


def insert_school(mongo_collection, **kwargs):
    """ insert a document into a collection """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
