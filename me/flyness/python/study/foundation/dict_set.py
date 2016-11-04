#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict
d = {'张三': 99, '李四': 66, '王五': 88}

d['张三'] = 33
print(d['张三'])
# print(d['王麻子'])
print('王麻子' in d)
print(d.get('王麻子'))
print(d.get('王麻子', -1))

d.pop('张三')
print(d)


#set
s = set([1, 2, 3])
print(s)

s.add(4)
print(s)

s.remove(3)
print(s)

s1 = set([1, 2, 3, 5, 6, 7, 8])
s2 = set([5, 2, 4, 6, 8, 9])
print(s1 & s2)
print(s1 | s2)


