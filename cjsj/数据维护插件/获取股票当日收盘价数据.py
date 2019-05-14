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

#建立连接
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg',
    charset='utf8'
)

#调用jqdata获取数据
df=jq.get_all_securities(date=d );
# 获取游标
cursor = connect.cursor()
#数据整理
df.reset_index(inplace=True,drop=False)
df.rename(columns={'index':'dm'},inplace=True)

for i in range(0, len(df)):#len(df)
    df1=jq.get_price(df.iloc[i]['dm'],  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
    df1.reset_index(inplace=True,drop=False)
    list=df1.values.tolist()

    #插入数据 
    for j in range(len(list)):
        sql = "INSERT INTO %s (date,open,close,high,low,volume) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )"
        date = datetime.date(datetime.fromtimestamp(list[j][0].timestamp()))        
        data = ('TB'+df.iloc[i]['dm'][:6],date,list[j][1],list[j][2],list[j][3],list[j][4],list[j][5])
        cursor.execute(sql % data)
        connect.commit()
    print(df.iloc[i]['dm'][:6]+'历史数据获取完成')

# 关闭连接
cursor.close()
connect.close()