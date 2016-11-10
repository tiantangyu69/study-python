#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 11, 11, 11, 11, 11)
print(dt)

# datetime convert to timestamp, 小数点后为毫秒数
print(now.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# str convert to datetime
cday = datetime.strptime('2016-11-11 11:10:00', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime convert to str
print(now.strftime('%a, %b %d %H:%M'))

# datetime delta
print(now + timedelta(hours=1))
print(now - timedelta(days=1))

# convert to UTC time
tz_utc_8 = timezone(timedelta(hours=8))
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
