#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'lizhitao'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('to many arguments')


if __name__ == '__main__':
    test()
