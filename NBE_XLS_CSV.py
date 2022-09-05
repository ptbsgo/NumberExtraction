# -*- coding: utf-8 -*-
# @Time    : 2022/9/5 12:08
# @Author  : ptbs
# @File    : NBE_XLS.py
# @Software: PyCharm
# ---------CODE-------------

def readcsv():
    import pandas as pd
    import os
    while True:
        filename = input("请输入文件路径（.csv文件）：")  # 文件路径
        if os.path.exists(filename):
            # 读取 用户账号   游戏名称  游戏金额  组成一个新表
            df_obj = pd.read_csv(filename, usecols=[1, 10], encoding='gbk')  # 读取 用户账号   游戏名称  游戏金额 列
            df_obj_data_sum = df_obj.groupby(['用户账号'], as_index=False)['游戏金额'].sum()  # 相同用户名 的金额 求和
            df_obj_data_sum.sort_values('游戏金额', inplace=True, ascending=False)  # 按金额降序  ，inplace 是是否再原有得表进行
            df_obj_data_sum.to_csv('./tmp/tmp.csv', index=False)  # 不输出索引  输出按金额排序好了得所有充值账号
            # 用户名和金额转成字典 用户名:金额
            df_obj_new = pd.read_csv('./tmp/tmp.csv', encoding='utf-8')
            user_money = dict(zip(df_obj_new['用户账号'], df_obj_new['游戏金额']))
            break
        else:
            print("路径不存在！，请重新输入！")
    return user_money



def judge_phone_and_qq_number(accounts:dict):
    import re
    import pandas as pd
    phone_list = []
    qq_list = []
    qq_money_list = []
    phone_money_list = []
    phone_dict = {}
    qq_dict = {}
    try:
        for key in accounts:
            p = re.findall('(13\d{9}|14[5|7|9]\d{8}|15\d{9}|166\d{8}|17[1|3|5|6|7|8]\d{8}|18\d{9}|19[9|8]\d{8})',key, re.S)
            if p == []:
                q = re.findall('[1-9][0-9]{4,12}', key, re.S)                #re正则识别QQ  不确定QQ 最长位数
                if q != []:
                    qq_list.append(int(q[0]))
                    qq_money_list.append(accounts[key])
                    qq_dict['qq号码（可能）'] = qq_list
                    qq_dict['充值金额'] = qq_money_list
            else:
                phone_list.append(int(p[0]))
                phone_money_list.append(accounts[key])
                phone_dict['手机号码'] = phone_list
                phone_dict['充值金额'] = phone_money_list
        # print(phone_dict)
        # print(qq_dict)
        phone_csv = pd.DataFrame.from_dict(phone_dict)
        qq_csv = pd.DataFrame.from_dict(qq_dict)
        phone_csv.to_csv('./tmp/phone.csv', index=False)  # 不输出索引    按金额排序输出电话
        qq_csv.to_csv('./tmp/qq.csv', index=False)  # 不输出索引     按金额排序输出QQ
        print("成功！")
    except PermissionError:
        print("You don't have permission to access this file.")




if __name__ == '__main__':
    judge_phone_and_qq_number(readcsv())