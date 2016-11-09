#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO

f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world'))
print(f.getvalue())

f = StringIO('this is a StringIO content\nhi\naaaaa')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
