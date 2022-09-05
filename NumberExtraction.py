# -*- coding: utf-8 -*-
# @Time    : 2022/9/2 2:58
# @Author  : ptbs
# @File    : NumberExtraction.py
# @Software: PyCharm
# ---------CODE-------------

# vname = lambda v, nms: [vn for vn in nms if id(v) == id(nms[vn])][0]  #获取变量的名称 ，没有解决通过一个write函数来解决文件名不同的方法。。。

def open_file():    #读文件
    phones = input("请输入文件夹路径地址：")
    # pwd = "./phone.txt"
    try:
        f = open(phones, "r",encoding="utf-8")
        content = f.readlines()
        f.close()
        payload_url = []
        for i in range(0, len(content)):
             payload_url.append(content[i].rstrip('\n'))
            # payload_url.append(content[i])
        return payload_url
    except FileNotFoundError:
        print("File is not found.")
    except PermissionError:
        print("You don't have permission to access this file.")

def write_files(phones:list,name):   #写phone.txt  第一个参数为列表，第二个为文件名
    import os
    dirs = "./tmp"
    if not os.path.exists(dirs):
        os.mkdir(dirs)
    else:
        f = open('./tmp/' + str(name) + '.txt','a',encoding="utf-8")
        for phone in phones:
            f.write(phone + "\n")
        f.close()


# 正则匹配手机号 和 QQ 号码(可能)
# print(re.findall('[1-9][0-9]{4,13}',s,re.S))
def judge_phone_and_qq_number(accounts):
    import re
    phone = []
    qq = []
    try:
        for account in accounts:
            p = re.findall('(13\d{9}|14[5|7|9]\d{8}|15\d{9}|166\d{8}|17[1|3|5|6|7|8]\d{8}|18\d{9}|19[9|8]\d{8})',  #re正则 识别手机
                           account, re.S)
            if p == []:
                q = re.findall('[1-9][0-9]{4,12}', account, re.S)                #re正则识别QQ  不确定QQ 是否最长13位
                qq.extend(q)
            else:
                phone.extend(p)
            # print(phone)
        write_files(phone,'phone')
        # print(qq)
        write_files(qq,'qq')
        print("成功！")
    except PermissionError:
        print("You don't have permission to access this file.")



if __name__ == '__main__':
     judge_phone_and_qq_number(open_file())
