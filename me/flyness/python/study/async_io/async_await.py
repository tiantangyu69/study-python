#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio


# 新语法只能用在Python 3.5以及后续版本
async def hello():
    print('Hello world!')
    r = await asyncio.sleep(1)
    print('hello again')
