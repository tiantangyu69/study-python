#!/usr/bin/env python3
# -*- coding: utf-8 -*-


age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

if None:
    print(None)

if "":
    print("空字符串")

if " ":
    print("空字符串")

if 0:
    print("0")

if []:
    print("[]")

if ():
    print("()")

s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
