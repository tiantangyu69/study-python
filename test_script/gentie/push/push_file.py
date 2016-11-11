#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


class GenUserFile(object):
    def gen_senior_user(self):
        f = open('D:\\gen_senior_user.txt', 'w')
        try:
            for n in range(100000):
                f.write(str(random.randint(1000000, 200000000)) + '\n')
        finally:
            f.close()

    def gen_m_user(self):
        f = open('D:\\gen_m_user.txt', 'w')
        try:
            for n in range(100000):
                f.write(str(random.randint(1000000, 200000000)) + '\n')
        finally:
            f.close()


if __name__ == '__main__':
    gen = GenUserFile()
    gen.gen_senior_user()
    gen.gen_m_user()
