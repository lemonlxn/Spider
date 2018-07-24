# /usr/bin/env python
# -*- coding:utf-8 -*-

# @Time    : 2018/7/5 20:42
# @Author  : lemon

def is_key_or_isbn(q):
    key_or_isbn = 'key'
    if q.isdigit() and len(q) == 13:
        key_or_isbn = 'isbn'

    short_q = q.replace('-','')
    if '-' in q and short_q.isdigit() and len(short_q) == 10:
        key_or_isbn = 'isbn'

    return key_or_isbn

