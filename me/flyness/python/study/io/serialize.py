#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import json

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('d:\\dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('d:\\dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系


json_str = json.dumps(d)
print(json_str)

print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('lizhitao', 27, 99)
print(json.dumps(s, default=student2dict))
json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print(json_str)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(json_str, object_hook=dict2student))
