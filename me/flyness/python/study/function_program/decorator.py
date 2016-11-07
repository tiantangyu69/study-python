#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools


# def now():
#     print('2016-11-02')
#
#
# f = now
# f()
#
# print(now.__name__)
# print(f.__name__)


# def log(func):
#     def wrapper(*args, **kw):
#         print("call %s()" % func.__name__)
#         return func(*args, **kw)
#
#     return wrapper
#
#
# @log
# def now():
#     print('2016-11-02')
#
#
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print("%s %s:" % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s:" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2016-11-02')


# f = now
# f()
if __name__ == '__main__':
    now()
    print(now.__name__)
