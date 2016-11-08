#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from me.flyness.python.study.advanced_oop.hello import Hello

h = Hello()
h.hello()
print(type(Hello))
print(type(h))


def fn(self, name='world'):
    print('hello, %s' % name)


Hello2 = type('Hello2', (object,), dict(hello=fn))

h1 = Hello2()
h1.hello()
print(type(Hello2))
print(type(h1))
