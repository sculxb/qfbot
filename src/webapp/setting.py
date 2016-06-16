#!/usr/bin/env python
# coding=utf-8
# vim: set et sw=4 ts=4 sts=4
# Author: YuanLin
# Created: 2016-05-04 17:31 CST


import os
import socket
import uuid


PORT = 8888

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "qfbot"
HOST = "http://127.0.0.1:8055/"
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
DEBUG = True

# redis
REDIS_URI = "redis://localhost:6379/1"
REDIS_SERVER = 'localhost'
REDIS_PORT = 6379

# cookie str
COOKIE_STR = uuid.uuid4().get_hex()
# COOKIE_STR = "SNDSFNWOEISDFFWF82392"


AVATAR_DEFAULT = [
    "1.jpeg",
]


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

STATIC = os.path.join(ROOT, "webapp/static")
TEMPLATE = os.path.join(ROOT, "webapp/template")

USER_ONE = {
    "username": "qfbot",
    "email": "i@qfbot.org",
    "password": "xxxxxxxx",
    "role": 777,
}
