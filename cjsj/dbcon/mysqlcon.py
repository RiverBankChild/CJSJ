'''
Created on 2019年4月30日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import pymysql.cursors
import jqdatasdk as jq
 
#jqdata认证
jq.auth('13401179853','king179853')

#调用jqdata获取数据
df=jq.get_all_securities(date='2019-04-30');

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
for i in range(len(list)):
    sql = "INSERT INTO dmb (dm,name) VALUES ( '%s', '%s')"
    data = (list[i][0],list[i][1])
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
connect.close()