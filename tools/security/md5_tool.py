# -*- coding:utf-8 -*-
# Author : Longhai
import hashlib

def md5_passwd(str,key='123456'):
    #satl是盐值，默认是123456
    str=str+key
    md = hashlib.md5()  # 构造一个md5对象
    md.update(str.encode())
    res = md.hexdigest()
    return res
