#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# list
names = ['aaa', 'bbb', 'ccc']
print(names)

print(len(names))
print(names[0])
print(names[-1])
names.append('ddd')
print(names)
names.insert(1, 'eeee')
print(names)
names.pop()
print(names)
names.pop(2)
print(names)
names[1] = 'lizhitao'
print(names)

L = [1, True, 'lizhitao']
print(L)

LL = [1, True, 'lizhitao', ['a', 'b', 'c'], 1.1]
print(len(LL))

L = []
print(len(L))


# tuple like readonly list
names = ('张三', '李四', '王五')
print(names)

t = (1,)
print(t)
