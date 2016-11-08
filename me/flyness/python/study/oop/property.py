#!/usr/bin/env python3
# -*- coding: utf-8-*-


class Student(object):
    name = 'lizhitao'

    def __init__(self, name):
        self.name = name


s = Student('bob')
s.score = 90

print(Student.name)
print(s.name)

del s.name
print(s.name)
print(Student.name)
