#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print(sorted([-3, 54, 4523, 5, 56, -345]))
print(sorted([-3, 54, 4523, 5, 56, -345], key=abs))

print(sorted(['sdgg', 'sgdg', 'wbheth', 'h34g34', 'Adgf', 'HG']))
print(sorted(['sdgg', 'sgdg', 'wbheth', 'h34g34', 'Adgf', 'HG'], key=str.lower, reverse=True))
