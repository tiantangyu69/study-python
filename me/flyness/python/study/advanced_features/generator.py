#!/usr/bin/env python3
# -*- coding: utf-8 -*-


g = (x * x for x in range(10))
print(g)

for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)

for n in f:
    print(n)
