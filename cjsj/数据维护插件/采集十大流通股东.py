'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
from jqdatasdk import finance
 
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


#获取十大流通股东
dm_list=[]
date_list=[]
#获取报告期数据
rq_list=['2015-03-31','2015-06-30','2015-09-30','2015-12-31',
         '2016-03-31','2016-06-30','2016-09-30','2016-12-31',
         '2017-03-31','2017-06-30','2017-09-30','2017-12-31',
         '2018-03-31','2018-06-30','2018-09-30','2018-12-31',
         '2019-03-31']
#获取dm数据
sql = "SELECT dm FROM dmb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    dm_list.append(row)
for i in range(0,len(dm_list)):    
    if dm_list[i][0].startwith('6'):
        dm_list[i][0]=dm_list[i][0]+'.XSHG'
    else:
        dm_list[i][0]=dm_list[i][0]+'.XSHE'

#获取日期数据
sql = "SELECT date FROM rqb order by id "
cursor.execute(sql)
for r in cursor.fetchall():
    date_list.append(r) 

#主体部分
for x in range(0,len(dm_list)):
    df3=finance.run_query(jq.query(
    finance.STK_SHAREHOLDER_FLOATING_TOP10.code,
    finance.STK_SHAREHOLDER_FLOATING_TOP10.shareholder_rank,
    finance.STK_SHAREHOLDER_FLOATING_TOP10.share_ratio
    ).filter(
    finance.STK_SHAREHOLDER_FLOATING_TOP10.code==dm_list[x][0],
    finance.STK_SHAREHOLDER_FLOATING_TOP10.end_date=='2015-03-31'#03-31 #06-30 #09-30 #12-31   
))
print(df3)


# 关闭连接
cursor.close()
connect.close()