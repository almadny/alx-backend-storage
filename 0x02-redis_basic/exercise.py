#!/usr/bin/env python3
""" Stores the cache class """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache Class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates and returns a random key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
