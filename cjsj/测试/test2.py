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
dm_sh_list=[]
sql = "SELECT dm FROM dmb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    dm_list.append(row) 
for s in range(len(dm_list)):
    if dm_list[s][0].startswith('6'):
        t=dm_list[s][0]+'.XSHG'
    else:
        t=dm_list[s][0]+'.XSHE'        
    dm_sh_list.append(t)
for x in range(0,len(dm_sh_list)):
    df=finance.run_query(
        jq.query(finance.STK_XR_XD.code,finance.STK_XR_XD.a_xr_date).filter(finance.STK_XR_XD.code==x).order_by(finance.STK_XR_XD.report_date.desc()).limit(1)
        )
    print(df)



# 关闭连接
cursor.close()
connect.close()