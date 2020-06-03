'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
from _datetime import datetime
 
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
sql3 = "SELECT close FROM tb603999 order by id desc limit 1 "
cursor.execute(sql3)
for row in cursor.fetchall():
    yz = row[0]

print(yz)

df1=jq.get_price("603999.XSHG",  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
df1.reset_index(inplace=True,drop=False)
lists=df1.values.tolist()
mbz = lists[len(lists)-1][2]

print(mbz)

if(yz==mbz):
    print("数据校验成功")
    pass
else:
    print("数据校验失败，请检查")



# 关闭连接
cursor.close()
connect.close()