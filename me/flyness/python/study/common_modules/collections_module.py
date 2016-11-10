#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

print('------------------------------ namedtuple -------------------------')
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('p.x: %s p.y %s' % (p.x, p.y))
print(isinstance(p, Point))
print(isinstance(p, tuple))

print('------------------------------ deque -------------------------')
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

print('------------------------------ defaultdict -------------------------')
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
# key2 不存在返回默认值 N/A
print(dd['key2'])

print('------------------------------ OrderedDict -------------------------')
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)


# FIFO dict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


print('------------------------------ Counter -------------------------')
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
