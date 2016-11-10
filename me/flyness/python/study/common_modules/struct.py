# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# import struct, io
#
# # >I 表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# print(struct.pack('>I', 10240099))
# # >IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
#
#
# # format
# # <         little-endian
# # >         big-endian
# # c         char            (1 byte)
# # I         unsigned int    (4 bytes)
# # H         unsigned short  (2 bytes)
#
#
# # 获取前30个字节(头字节)
# def get_header_bytes(path):
#     with io.open(path, 'rb') as file:
#         header_bytes = file.read(30)
#         print(header_bytes)
#         return header_bytes
#
#
# # 检查位图
# def check_bitmap(byte):
#     t = struct.unpack('<ccIIIIIIHH', byte)
#     if t[0:2] == (b'B', b'M'):
#         print('文件属于Windows位图')
#         print('文件大小: %d' % t[2])
#         print('分辨率: %d*%d' % (t[6], t[7]))
#         print('颜色数: %d' % t[9])
#     elif t[0:2] == (b'B', b'M'):
#         print('文件属于OS/2位图')
#     else:
#         print('文件类型未知')
#
#
# b = get_header_bytes('../../res/mvp.bmp')
# if len(b) == 30:
#     check_bitmap(b)
# else:
#     print('文件读取失败')
