# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 2:58
# @Author  : ptbs
# @File    : NumberExtraction.py
# @Software: PyCharm
# ---------CODE-------------
import re


# 正则匹配手机号
def judge_phone_number(account):
    a = re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', account)
    print(a)


if __name__ == '__main__':
    judge_phone_number('18921819332s')
