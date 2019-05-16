'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
 
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

#更新股票表结构#TIMESTAMP(8)　| YYYYMMDD
list_dm=[]
sql = "SELECT dm FROM dmb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    list_dm.append(row)

total=0;
for i in range(0,len(list_dm)):
    '''
    sql1="alter table %s add dm varchar(8)  default '未知代码',add ltsz  Float(14,2) default  0.00,add syl    Float(7,2)  default  0.00,add ys     Float(14,2) default  0.00,add jlr    Float(14,2) default  0.00,add cdd    Float(14,2) default  0.00,add dd    Float(14,2) default  0.00,add zd    Float(14,2) default  0.00,add xd    Float(14,2) default  0.00,add lt_1  Float(5,2) default  0.00,add lt_2  Float(5,2) default  0.00,add lt_3  Float(5,2) default  0.00,add lt_4  Float(5,2) default  0.00,add lt_5  Float(5,2) default  0.00,add lt_6  Float(5,2) default  0.00,add lt_7  Float(5,2) default  0.00,add lt_8  Float(5,2) default  0.00,add lt_9  Float(5,2) default  0.00,add lt_10  Float(5,2) default  0.00  ;"
    sql2="alter table %s modify column open Float(7,2) default  0.00;"
    sql3="alter table %s modify column close Float(7,2) default  0.00;"
    sql4="alter table %s modify column high Float(7,2) default  0.00;"
    sql5="alter table %s modify column low Float(7,2) default  0.00;"
    sql6="alter table %s modify column date  varchar(16) unique default '未知日期' ;"
    sql7="alter table %s change volume cjl Float(14,2) default  0.00;"
   
    data = ('TB'+list_dm[i][0])
    
    cursor.execute(sql1 % data)
    cursor.execute(sql2 % data)
    cursor.execute(sql3 % data)
    cursor.execute(sql4 % data)
    cursor.execute(sql5 % data)
    cursor.execute(sql6 % data)
    cursor.execute(sql7 % data)
    '''
    
    data = ('TB'+list_dm[i][0])
    sql="ALTER TABLE %s ADD zdf  Float(5,2) default  0.00;"
    cursor.execute(sql % data)
    connect.commit()
    print(data+'修改成功')
    total=total+1
print('成功修改', total, '张表')

# 关闭连接
cursor.close()
connect.close()