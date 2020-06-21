'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
from jqdatasdk import finance

#超参
jzrq='2020-06-05'

 
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

#获取报告期数据
rq_list_d=['2014-12-31',
         '2015-03-31','2015-06-30','2015-09-30','2015-12-31',
         '2016-03-31','2016-06-30','2016-09-30','2016-12-31',
         '2017-03-31','2017-06-30','2017-09-30','2017-12-31',
         '2018-03-31','2018-06-30','2018-09-30','2018-12-31',
         '2019-03-31','2019-06-30','2019-09-30','2019-12-31',
         '2020-03-31','2020-06-30','2020-09-30','2020-12-31',
         '2021-03-31','2021-06-30','2021-09-30','2021-12-31',
         '2022-03-31','2022-06-30','2022-09-30','2022-12-31',
         '2023-03-31','2023-06-30','2023-09-30','2023-12-31']

rq_int_list_d=[20141231,
         20150331,20150630,20150930,20151231,
         20160331,20160630,20160930,20161231,
         20170331,20170630,20170930,20171231,
         20180331,20180630,20180930,20181231,
         20190331,20190630,20190930,20191231,
         20200331,20200630,20200930,20201231,
         20210331,20210630,20210930,20211231,
         20220331,20220630,20220930,20221231,
         20230331,20230630,20230930,20231231]

rq_list=[]
rq_int_list=[]
for i in range(0,len(rq_int_list_d)-1):
    if(int(jzrq.replace('-',''))>rq_int_list_d[i] and int(jzrq.replace('-',''))<=rq_int_list_d[i+1]):
        rq_list=rq_list_d[0:i+2]
        rq_int_list=rq_int_list_d[0:i+2]
        break
    else:
        pass

#获取日期数据
date_list=[]
sql1 = "SELECT date FROM rqb order by id "
cursor.execute(sql1)
for it in cursor.fetchall():
    date_list.append(it)
    
date_int_list=[]
sql2 = "SELECT date FROM rqb order by id "
cursor.execute(sql2)
for row in cursor.fetchall():
    p=int(row[0].replace('-','').replace('\'', ''))        
    date_int_list.append(p) 

#获取dm数据
dm_list=[]
sql3 = "SELECT dm FROM dmb order by id "
cursor.execute(sql3)
for row in cursor.fetchall():
    if row[0].startswith('6'):
        r=row[0]+'.XSHG'
    else:
        r=row[0]+'.XSHE'        
    dm_list.append(r)  


#主体部分
for y in range(0,len(dm_list)):
    total=0;
    for x in range(len(rq_list)): 
        ltgd_df=finance.run_query(jq.query(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.shareholder_rank,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.share_ratio
        ).filter(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code==dm_list[y],
        finance.STK_SHAREHOLDER_FLOATING_TOP10.end_date==rq_list[x]  
        ))
        for z in range(len(date_int_list)):
            if date_int_list[z]>rq_int_list[x] and date_int_list[z]<=rq_int_list[x+1]:
                sql = "  update %s set lt_1=%.2f , lt_2=%.2f  ,lt_3=%.2f  ,lt_4=%.2f  ,lt_5=%.2f  ,lt_6=%.2f  ,lt_7=%.2f  ,lt_8=%.2f  ,lt_9=%.2f  ,lt_10=%.2f    where date='%s'"
                try:
                    data=('TB'+dm_list[y][:6],ltgd_df.iloc[0]['share_ratio'],ltgd_df.iloc[1]['share_ratio'],ltgd_df.iloc[2]['share_ratio'],ltgd_df.iloc[3]['share_ratio'],ltgd_df.iloc[4]['share_ratio'],ltgd_df.iloc[5]['share_ratio'],ltgd_df.iloc[6]['share_ratio'],ltgd_df.iloc[7]['share_ratio'],ltgd_df.iloc[8]['share_ratio'],ltgd_df.iloc[9]['share_ratio'],date_list[z][0])
                    cursor.execute(sql % data)
                except Exception as e:
                    connect.rollback()  # 事务回滚
                    continue
                else:
                    connect.commit()  # 事务提交
                    total=total+cursor.rowcount
    print(dm_list[y],'数据插入完毕，共更新了',total,'条数据')   
print('所有数据插入完毕')         

# 关闭连接
cursor.close()
connect.close()