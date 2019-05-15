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

dm_list=['000001','000002']

# 插入数据
total=0;
for i in range(len(dm_list)):
    sql = "create table IF NOT EXISTS %s  (id int primary key auto_increment);"    
    data = 'TB'+dm_list[i]
    print(sql)
    print(data)
    cursor.execute(sql % data)
    break
    connect.commit()
    print(data+'创建成功')
    total=total+1
print('成功创建', total, '张表')

# 关闭连接
cursor.close()
connect.close()