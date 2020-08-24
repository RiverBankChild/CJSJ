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
    sql = "create table IF NOT EXISTS %s (\
    id int primary key auto_increment,\
    dm varchar(8)  default '未知代码',\
    date varchar(16) unique default '未知日期',\
    open Float(7,2) default  0.00,\
    close Float(7,2) default  0.00,\
    high Float(7,2) default  0.00,\
    low Float(7,2) default  0.00,\
    zdf  Float(6,2) default  0.00,\
    cjl Float(14,2) default  0.00,\
    ltsz   Float(14,2) default  0.00,\
    syl    Float(10,2)  default  0.00,\
    ys     Float(14,2) default  0.00,\
    jlr    Float(14,2) default  0.00,\
    cdd    Float(14,2) default  0.00,\
    dd    Float(14,2) default  0.00,\
    zd    Float(14,2) default  0.00,\
    xd    Float(14,2) default  0.00,\
    lt_1  Float(5,2) default  0.00,\
    lt_2  Float(5,2) default  0.00,\
    lt_3  Float(5,2) default  0.00,\
    lt_4  Float(5,2) default  0.00,\
    lt_5  Float(5,2) default  0.00,\
    lt_6  Float(5,2) default  0.00,\
    lt_7  Float(5,2) default  0.00,\
    lt_8  Float(5,2) default  0.00,\
    lt_9  Float(5,2) default  0.00,\
    lt_10  Float(5,2) default  0.00\
    );"   
    data = ('TB'+dm_list[i][0])
    cursor.execute(sql % data)
    connect.commit()
    print(data+'创建成功')
    total=total+1
print('成功创建', total, '张表')

# 关闭连接
cursor.close()
connect.close()