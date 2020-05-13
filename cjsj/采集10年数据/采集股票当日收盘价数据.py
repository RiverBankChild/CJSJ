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
ksrq='2009-11-05'
jsrq='2020-04-29'  
 
 
 
 
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
    db='xg2',
    charset='utf8'
)
cursor = connect.cursor()

#获取现有dm数据
dm_list=[]
sql3 = "SELECT dm FROM dmb order by id "
cursor.execute(sql3)

for row in cursor.fetchall():
    if row[0].startswith('6'):
        r=row[0]+'.XSHG'
    else:
        r=row[0]+'.XSHE'        
    dm_list.append(r)  

#dm_list=['603577.XSHG']
for i in range(0, len(dm_list)):
    df1=jq.get_price(dm_list[i],  start_date=ksrq, end_date=jsrq, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
    df1.reset_index(inplace=True,drop=False)
    list=df1.values.tolist()
    for j in range(len(list)):
        sql = "INSERT INTO %s (date,open,close,high,low,cjl) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )"
        date = datetime.date(datetime.fromtimestamp(list[j][0].timestamp()))        
        data = ('TB'+dm_list[i][:6],date,list[j][1],list[j][2],list[j][3],list[j][4],list[j][5])
        cursor.execute(sql % data)
        connect.commit()  # 事务提交  
    print(dm_list[i][:6]+'历史收盘价获取完成')
print('所有历史收盘价获取完成')

# 关闭连接
cursor.close()
connect.close()