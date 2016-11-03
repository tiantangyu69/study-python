# https://pypi.python.org/pypi
# 使用 pip3 install libname 安装第三方模块
# pip3 install Pillow 这是Python下非常强大的处理图像的工具库

from PIL import Image
import sys

im = Image.open('cymbals.png')
print(im.format, im.size, im.mode)

im.thumbnail((60, 60))
im.save('thumb.png', 'PNG')


print(sys.path)
