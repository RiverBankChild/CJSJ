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
print('今天是'+d)


#建立连接
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg',
    charset='utf8'
)


# 获取游标
cursor = connect.cursor()

total=0;

#更新日期表
list5=[]
sql = "SELECT date FROM szzs order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    list5.append(row)
for k in range(0,len(list5)):
    try:
        sql = "INSERT INTO rqb (date) VALUES ( '%s')"
        datek =list5[k]         
        datak = (datek)
        cursor.execute(sql % datak)
    except Exception as e:
        connect.rollback()  # 事务回滚
        continue
    else:
        connect.commit()  # 事务提交
        total=total+cursor.rowcount
print('日期表更新完成，共更新了',total,'条数据')
         


# 关闭连接
cursor.close()
connect.close()