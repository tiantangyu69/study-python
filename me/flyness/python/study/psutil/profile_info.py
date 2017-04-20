#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import psutil, datetime

# 1mb 字节数
oneMb = 1024 * 1024

# 获取系统性能信息
print("cpu times: ", psutil.cpu_times())
print("cpu times per cpu: ", psutil.cpu_times(percpu=True))
print("cpu stats: ", psutil.cpu_stats())
print("cpu count: ", psutil.cpu_count())
print("cpu count without logical count: ", psutil.cpu_count(logical=False))  # 获取 CPU 的物理个数

# 获取系统内存信息
mem = psutil.virtual_memory()
print("system total memory: %d MB, used memory: %d MB" % (mem.total / oneMb, mem.used / oneMb))
print(mem)
print(psutil.swap_memory())

# 磁盘信息
print(psutil.disk_partitions())
print(psutil.disk_usage("/"))
print(psutil.disk_io_counters(perdisk=True))

# 网络信息
print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))

# 其他系统信息
print(psutil.users())
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))
