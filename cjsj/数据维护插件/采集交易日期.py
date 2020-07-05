'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import chinese_calendar
import pandas as pd
 

 
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



date_list=[]
rm_list=[]
e = pd.bdate_range('01/01/2020', '12/30/2020')
datedf=e.date #获取日期列表

date_list=datedf.tolist()


for d in date_list:
    if chinese_calendar.is_holiday(d):
        rm_list.append(d)
    else:
        pass
    
    

for t in rm_list:

    date_list.remove(t)
    
    
for i in date_list:

    print(i)
    
print('交易总天数：',len(date_list))


total = 0
for k in range(0,len(date_list)):
    try:
        sql = "INSERT INTO jyrqb (jyrq) VALUES ( '%s')"
        data = date_list[k]
        cursor.execute(sql % data)
    except Exception as e:
        connect.rollback()  # 事务回滚
    else:
        connect.commit()  # 事务提交
        total=total+cursor.rowcount
print('交易日期表更新完成，共更新了',total,'条数据')


# 关闭连接
cursor.close()
connect.close()