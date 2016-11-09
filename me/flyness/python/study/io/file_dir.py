#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

print(os.name)
# print(os.uname())
print(os.environ)
print(os.environ.get('JAVA_HOME', 'default'))
print(os.path.abspath('.'))
print(os.path.join('d:\\aaa', 'test'))
print(os.mkdir('d:/abcedsfdfsdf'))
print(os.rmdir('d:/abcedsfdfsdf'))
print(os.path.split('d:\\aaa\\cc'))
print(os.path.splitext('d:\\aaa\\cc.txt'))
# os.rename("D:\\test_write.txt", 'D:\\test_write_read.txt')
# os.remove("d:\\binary.txt")

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
