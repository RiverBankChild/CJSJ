'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq

 
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


'''
#获取总市值和净利润
date_list=[]
sql = "SELECT date FROM rqb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    date_list.append(row)
for k in range(0,len(date_list)):
    df_volandincome = jq.get_fundamentals(jq.query(
    jq.valuation.code, 
    jq.valuation.circulating_market_cap, 
    jq.valuation.pe_ratio, 
    jq.income.total_operating_revenue,
    jq.income.np_parent_company_owners 
    ), date=date_list[k][0])
    volandincome_list=df_volandincome.values.tolist()
    total=0;
    for l in range(0,len(volandincome_list)):
        try:
            sql = "update %s set dm='%s'  , ltsz=%.2f ,  syl=%.2f  ,  ys=%.2f  ,  jlr=%.2f  where date='%s'"
            dataall=('TB'+volandincome_list[l][0][:6],volandincome_list[l][0][:6],volandincome_list[l][1],volandincome_list[l][2],volandincome_list[l][3],volandincome_list[l][4],date_list[k][0])
            cursor.execute(sql % dataall)
        except Exception as e:
            connect.rollback()  # 事务回滚
        else:
            connect.commit()  # 事务提交
            total=total+cursor.rowcount
    print(date_list[k][0],'数据插入完毕','共更新了',total,'条数据')
print("所有数据插入完成")
'''

'''
#获取每日大单量,最上面的数据是最新的
dmb_list=[]
sql = "SELECT dm FROM dmb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    dmb_list.append(row)
for o in range(0,len(dmb_list)):
    zjl_df=jq.get_money_flow([dmb_list[o][0]]+'.XSHE', start_date='2015-01-01', end_date='2019-05-15', fields=['date','net_amount_xl','net_amount_l','net_amount_m','net_amount_s'])
    print(zjl_df)
    zjl_list=zjl_df.values.tolist()
    total=0;
    for p in range(0,len(zjl_list)):
        try:
            sql = "update %s set  cdd=%.2f ,  dd=%.2f  ,  zd=%.2f  ,  xd=%.2f  where date='%s'"
            data_zjl=('TB'+dmb_list[o][0],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],zjl_list[p][0])
            cursor.execute(sql % data_zjl)
        except Exception as e:
            connect.rollback()  # 事务回滚
        else:
            connect.commit()  # 事务提交
            total=total+cursor.rowcount
    print(dmb_list[o][0],'数据插入完毕','共更新了',total,'条数据')
print("所有数据插入完成")
'''



#获取十大流通股东
dm_list=[]
rq_list=['2015-03-31','2015-06-30','2015-09-30','2015-12-31',
         '2016-03-31','2016-06-30','2016-09-30','2016-12-31',
         '2017-03-31','2017-06-30','2017-09-30','2017-12-31',
         '2018-03-31','2018-06-30','2018-09-30','2018-12-31',
         '2019-03-31']
sql = "SELECT dm FROM dmb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    dm_list.append(row) 
from jqdatasdk import finance
for x in range(0,len(dm_list)):
    df3=finance.run_query(jq.query(
    finance.STK_SHAREHOLDER_FLOATING_TOP10.code,
    finance.STK_SHAREHOLDER_FLOATING_TOP10.shareholder_rank,
    finance.STK_SHAREHOLDER_FLOATING_TOP10.share_ratio
    ).filter(
    finance.STK_SHAREHOLDER_FLOATING_TOP10.code==dm_list[x][0]+'.XSHE',
    finance.STK_SHAREHOLDER_FLOATING_TOP10.end_date=='2015-03-31'#03-31 #06-30 #09-30 #12-31   
))
print(df3)




# 关闭连接
cursor.close()
connect.close()