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
#调用jqdata获取数据
df=jq.get_all_securities(date=d );

#数据整理
df.reset_index(inplace=True,drop=False)
df.rename(columns={'index':'dm'},inplace=True)
for i in range(0, len(df)):
    df1=jq.get_price(df.iloc[i]['dm'],  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=False, fq='pre')
    df1.reset_index(inplace=True,drop=False)
    print(df1)
#list=df.values.tolist()

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

# 插入数据
for i in range(len(list)):
    sql = "INSERT INTO dmb (dm,name) VALUES ( '%s', '%s')"
    data = (list[i][0],list[i][1])
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
connect.close()