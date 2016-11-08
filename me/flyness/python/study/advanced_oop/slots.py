#!/usr/bin/env python3
# -*- coding: utf-8-*-
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Michael'  # 给实例绑定一个属性
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
print(s.age)


# s2 = Student()
# s2.set_age(25)

def set_score(self, score):
    self.score = score


Student.set_score = set_score
s3 = Student()
s3.set_score(11)
print(s3.score)


# 使用 __slot__ 限制实例的属性，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99
