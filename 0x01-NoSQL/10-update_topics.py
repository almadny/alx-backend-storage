#!/usr/bin/env python3
""" Contains Python function that inserts a document into a collection"""


def update_topics(mongo_collection, name, topics):
    """ insert a document into a collection """
    mongo_collection.update_many({"name": name}, {'$set': {"topics": topics}})
