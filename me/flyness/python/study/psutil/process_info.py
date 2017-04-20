#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil
from subprocess import PIPE

print(psutil.pids())  # 列出所有进程 pid
p = psutil.Process(731)
print(p.name())  # 进程名
print(p.exe())  # 进程 bin 路径
print(p.cwd())  # 进程工作目录绝对路径
print(p.status())  # 进程状态
print(p.create_time())  # 进程创建时间
print(p.uids())
print(p.gids())
print(p.cpu_times())
# print(p.cpu_affinity())
print(p.memory_percent())
print(p.memory_info())
# print(p.io_counters())
print(p.connections())
print(p.num_threads())

p2 = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
print(p2.name())
print(p2.username())
print(p2.communicate())
print(p.cpu_times())