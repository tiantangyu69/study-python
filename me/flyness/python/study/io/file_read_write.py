#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    f = open('d:\\d2f42068.ini', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('d:\\d2f42068.ini', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

with open('d:\\binary.txt', 'rb') as f:
    print(f.read())

f = open('d:\\test_write.txt', 'w')
f.write('Hello world!')
f.close()

with open('d:\\test_write.txt', 'a') as f:
    f.write('\nHello, world!')
