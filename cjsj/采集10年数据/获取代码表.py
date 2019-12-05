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

#建立连接获取游标
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg2',
    charset='utf8'
)
cursor = connect.cursor()

#调用jqdata获取数据
df=jq.get_all_securities(date=d );

#数据整理
df.drop(columns=['start_date', 'end_date','type','name'],axis=1,inplace=True);
df.rename(columns={'display_name':'name'},inplace=True)
df.reset_index(inplace=True,drop=False)
df.rename(columns={'index':'dm'},inplace=True)
for i in range(0, len(df)):
    df.iloc[i]['dm']=df.iloc[i]['dm'][:6] 
list=df.values.tolist()

sql1="truncate table dmb"
cursor.execute(sql1)
connect.commit()

# 插入数据
total=0;
for i in range(len(list)):
    sql = "INSERT INTO dmb (dm,name) VALUES ( '%s', '%s')"
    data = (list[i][0],list[i][1])
    cursor.execute(sql % data)
    connect.commit()
    total=total+cursor.rowcount
print('成功获取', total, '支股票')

# 关闭连接
cursor.close()
connect.close()