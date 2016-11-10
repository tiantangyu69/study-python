#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install mysql-connector 安装 mysql connector
import mysql.connector

# config = {'host': '10.120.153.229',
#           'user': 'comments',
#           'password': 'comments',
#           'port': 6000,  # 默认即为3306
#           'database': 'general-comments-test',
#           'charset': 'utf8'  # 默认即为utf8
#           }
#
# try:
#     conn = mysql.connector.connect(**config)
#     cursor = conn.cursor()
#     cursor.execute('SELECT id, deviceType FROM DeviceInfo LIMIT 10')
#     # for id, deviceType in cursor:
#     #     print(id, deviceType)
#     # values = cursor.fetchall()
#     # print(values)
# except mysql.connector.Error as e:
#     print('fails!{}'.format(e))
# finally:
#     cursor.close()
#     conn.close()


config = {'host': '10.234.129.138',
          'user': 'root',
          'password': '123456',
          'port': 3306,  # 默认即为3306
          'database': 'assess',
          'charset': 'utf8'  # 默认即为utf8
          }

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM channel LIMIT 10')
    # for id, deviceType in cursor:
    #     print(id, deviceType)
    values = cursor.fetchall()
    print(values)
except mysql.connector.Error as e:
    print('fails!{}'.format(e))
finally:
    cursor.close()
    conn.close()
