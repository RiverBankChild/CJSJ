'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
from _datetime import datetime
 
#超参
jzrq='2020-06-05'
 
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

#获取现有dm数据
dm_list=[]
sql3 = "SELECT dm FROM dmb order by id "
cursor.execute(sql3)
for row in cursor.fetchall():
    r=row[0]      
    dm_list.append(r)  
    
id_list=[]
for i in range(0, len(dm_list)):
    id_list = []
    
    sql2 = "SELECT id FROM %s order by id "
    data = ('TB'+dm_list[i][:6])
    cursor.execute(sql2 % data)
    for row in cursor.fetchall():
        r=row[0]      
        id_list.append(r) 
    
    for j in range(0,len(id_list)):
        zs = 0.00
        if j == 0 :
            pass
        else:
            sql0 = "SELECT close FROM %s where id = %d  "
            data = ('TB'+dm_list[i][:6],id_list[j-1])
            cursor.execute(sql0 % data)
            for row in cursor.fetchall():
                zs=row[0]      

        sql4 = "update %s set zs = %.2f where id = %d  "
        data = ('TB'+dm_list[i][:6],zs,id_list[j])
        cursor.execute(sql4 % data)
        connect.commit()  # 事务提交
    
    
    print(dm_list[i][:6]+'昨收获取完成')
print('所有昨收数据获取完成')

# 关闭连接
cursor.close()
connect.close()