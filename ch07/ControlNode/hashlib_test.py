# coding:utf-8
import hashlib

m1 = hashlib.md5()    # 构造hash对象
m1.update('hello')
m1.update(' ')
m1.update('python')

m2 = hashlib.md5('hello python')

print m1.hexdigest() == m2.hexdigest()    # 两种方式的效果相同