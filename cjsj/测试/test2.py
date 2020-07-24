'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
更新时间必须是下午5点以后或者是周末
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
from _datetime import datetime
from jqdatasdk import finance
import chinese_calendar
from os.path import  os
import datetime as dt


#认证
jq.auth('13401179853','king179853')

d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 

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




print("...............开始修正除权数据..............................")

syccqrq=''

sql = "SELECT cqrq FROM cqrqb where id =1 "
cursor.execute(sql)
 
syccqrq=cursor.fetchall()[0][0]

print("上一次除权日期为",syccqrq)

#获取需要除权的表
dm_list=[]
dm_sh_list=[]
dm_cq_list=[]
 
sql = "SELECT dm  FROM dmb  order by id "
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
        jq.query(finance.STK_XR_XD.code,finance.STK_XR_XD.a_xr_date,finance.STK_XR_XD.dividend_ratio,finance.STK_XR_XD.transfer_ratio).filter(finance.STK_XR_XD.code==dm_sh_list[x]).order_by(finance.STK_XR_XD.report_date.desc()).limit(1)
        )
    print(df)
    if(df.empty):
        print('empty')
        pass
    else:   
        for i in range(0, 1):
            if(str(df.iloc[i]['a_xr_date'])=='None'):
                print('NONE')
                pass
            else:
                if(int(str(df.iloc[i]['a_xr_date']).replace('-',''))>int(d.replace('-','')) or int(str(df.iloc[i]['a_xr_date']).replace('-',''))<=int(syccqrq.replace('-',''))):
                    print('未来除权或者已经除权')
                    pass
                else:
                    #if((str(df.iloc[i]['dividend_ratio'])!='None' or str(df.iloc[i]['transfer_ratio'])!='None')):
                    dm_cq_list.append(df.iloc[i]['code'][:6])
    





  

# 关闭连接
cursor.close()
connect.close()