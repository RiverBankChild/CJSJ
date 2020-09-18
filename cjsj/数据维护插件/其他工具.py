'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time

#jqdata认证
jq.auth('13401179853','king179853')

#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print(d)

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

#获取现有代码表
dm_list=[]
sql = "SELECT dm  FROM dmb order by id "
cursor.execute(sql)
for a in cursor.fetchall():
    dm_list.append(a)  


# 插入数据
total=0;
for i in range(len(dm_list)):
    #TIMESTAMP(8)　| YYYYMMDD
    sql = "ALTER TABLE %s   ADD COLUMN  zs Float(7,2) ,ADD COLUMN  fs text ;"   
    data = ('TB'+dm_list[i][0])
    cursor.execute(sql % data)
    connect.commit()
    print(data+'增加列成功')
    total=total+1
print('成功修改', total, '张表')

# 关闭连接
cursor.close()
connect.close()