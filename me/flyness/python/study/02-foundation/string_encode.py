#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('包含中文的str')

# ord() 获取字符的整数表示 chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))

print(chr(65))
print(chr(20013))

print('\u4e2d\u6587')

x = b'abc'
print('abc'.encode('utf-8'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len(b'abc'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'))
print(len('中文'.encode('utf-8')))


# format
print('hello %s' % 'world')
print('age: %d, name: %s' % (23, 'lizhitao'))
