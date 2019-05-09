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
df.drop(columns=['start_date', 'end_date','type','name'],axis=1,inplace=True);
df.rename(columns={'display_name':'name'},inplace=True)
df.reset_index(inplace=True,drop=False)
df.rename(columns={'index':'dm'},inplace=True)
for i in range(0, len(df)):
    df.iloc[i]['dm']=df.iloc[i]['dm'][:6] 
list=df.values.tolist()

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
total=0;
for i in range(len(list)):
    #TIMESTAMP(8)　| YYYYMMDD
    sql = " create table IF NOT EXISTS %s(id int primary key auto_increment,date varchar(16) unique ,open Float(5,2) default  0.00,close Float(5,2) default  0.00,high Float(5,2) default  0.00,low Float(5,2) default  0.00,volume Float(14,2) default  0.00);"
    data = ('TB'+list[i][0])
    cursor.execute(sql % data)
    connect.commit()
    print(data+'创建成功')
    total=total+1
print('成功创建', total, '张表')

# 关闭连接
cursor.close()
connect.close()