#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for loop
names = ['张三', '李四', '王五']

for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x

print(sum)

sum = 0
for x in range(10):
    sum = sum + x

print(sum)


# while loop
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
