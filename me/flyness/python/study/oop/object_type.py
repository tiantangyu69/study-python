# /usr/bin/env python3
# -*- coding:utf-8 -*-
import types

print(type(123))
print(type(''))
print(type(None))
print(type(abs))

print(type(123) == type(456))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)
# 获得一个对象的所有属性和方法
print(dir('ABC'))


class MyDog(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

# getattr()、setattr()以及hasattr()
print(hasattr(dog, 'x'))
print(dog.x)
print(hasattr(dog, 'y'))
setattr(dog, 'y', 19)
hasattr(dog, 'y')
print(getattr(dog, 'y'))
print(dog.y)
print(getattr(dog, 'z', 11))
print(hasattr(dog, 'power'))
print(getattr(dog, 'power'))
fn = getattr(dog, 'power')
print(fn())
