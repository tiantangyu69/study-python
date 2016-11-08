# /usr/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print("%s %s" % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


if __name__ == '__main__':
    s1 = Student('张三', 22)
    s1.print_score()
    s2 = Student('李四', 24)
    s2.print_score()

    s1.sex = '男'
    print(s1.sex)
    print(s1.get_name())
    # print(s1._Student.__name)
