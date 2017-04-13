#!/usr/bin/ python3.6

# -*- coding:utf-8 -*-

'''
Models for user, blog, comment.
'''

__authro__ = 'dingjiayi'

import time, uuid

# from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s' % (int(time.time()*1000), uuid.uuid4().hex)

a= time.time()
print(a)
b = uuid.uuid4()
c = b.hex
print(b)
print(c)
print(next_id())
