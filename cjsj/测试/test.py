'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
from jqdatasdk import finance

#超参
jzrq='2020-06-05'

 
#jqdata认证
jq.auth('13401179853','king179853')

#建立连接# 获取游标
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg',
    charset='utf8'
)
cursor = connect.cursor()

#获取日期数据
date_list=[]
sql1 = "SELECT fs FROM tb300860 order by id limit 1; "
cursor.execute(sql1)
for it in cursor.fetchall():
    date_list.append(it)

print(date_list)    
   

# 关闭连接
cursor.close()
connect.close()