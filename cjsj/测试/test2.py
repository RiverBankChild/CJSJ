'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time


#建立连接 获取游标
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg',
    charset='utf8'
)
cursor = connect.cursor()

dm_delete_list= [['000001', '平安银行']]

# 插入数据
total=0
for o in range(len(dm_delete_list)):
    sql = " drop table %s"
    data = ('TB'+dm_delete_list[o][0])
    print(data)
    cursor.execute(sql%data)
    connect.commit()
    total=total+cursor.rowcount
    print('成功删除', 'TB'+dm_delete_list[o][0])
print('成功删除', total, '张股票表')
# 关闭连接
cursor.close()
connect.close()