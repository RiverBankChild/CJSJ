'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
from jqdatasdk import finance
import time
from _datetime import datetime
 
#jqdata认证
jq.auth('13401179853','king179853')

print("...............开始修正除权数据..............................")
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

#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print('今天是'+d)

#获取最新日期表
date_new_list=[]
sql = "SELECT date FROM rqb order by id "
cursor.execute(sql)
for c in cursor.fetchall():
    date_new_list.append(c[0]) 


#获取报告期数据
rq_list=['2015-03-31','2015-06-30','2015-09-30','2015-12-31',
         '2016-03-31','2016-06-30','2016-09-30','2016-12-31',
         '2017-03-31','2017-06-30','2017-09-30','2017-12-31',
         '2018-03-31','2018-06-30','2018-09-30','2018-12-31',
         '2019-03-31','2019-06-30','2019-09-30','2019-12-31']
rq_int_list=[20150331,20150630,20150930,20151231,
         20160331,20160630,20160930,20161231,
         20170331,20170630,20170930,20171231,
         20180331,20180630,20180930,20181231,
         20190331,20190630,20190930,20191231]


#获取需要除权的表
dm_list=[]
dm_sh_list=[]
dm_cq_list=[]
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
                if(int(str(df.iloc[i]['a_xr_date']).replace('-',''))>int(d.replace('-',''))):
                    print('未来除权')
                    pass
                else:
                    if((str(df.iloc[i]['dividend_ratio'])!='None' or str(df.iloc[i]['transfer_ratio'])!='None')):
                        dm_cq_list.append(df.iloc[i]['code'][:6])
    print(dm_cq_list)
print(dm_cq_list)        
print("共需要更新",len(dm_cq_list),'张表')


#清空除权表
print("开始清空除权表数据....................")
for v in range(len(dm_cq_list)):
    sql_1 = "truncate table %s"
    data = ('TB'+dm_cq_list[v])
    try:
        cursor.execute(sql_1 % data)  
    except Exception as e:
        connect.rollback()  # 事务回滚
        print('事务处理失败', e)
    else:
        connect.commit()  # 事务提交
        print('TB'+dm_cq_list[v],'数据清空成功')


#3.向新增加的表中插入数据
print("开始向除权表中插入数据...................................................")
dm_insert_sh_list=[]
for s in range(len(dm_cq_list)):
    if dm_cq_list[s].startswith('6'):
        t=dm_cq_list[s]+'.XSHG'
    else:
        t=dm_cq_list[s]+'.XSHE'        
    dm_insert_sh_list.append(t)
for q in range(0, len(dm_cq_list)):
    #获取收盘价
    insert_df=jq.get_price(dm_insert_sh_list[q],  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
    insert_df.reset_index(inplace=True,drop=False)
    insert_list=insert_df.values.tolist()
    for s in range(len(insert_list)):
        sql = "INSERT INTO %s (date,open,close,high,low,cjl) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )" 
        date = datetime.date(datetime.fromtimestamp(insert_list[s][0].timestamp()))       
        data = ('TB'+dm_cq_list[q],date,insert_list[s][1],insert_list[s][2],insert_list[s][3],insert_list[s][4],insert_list[s][5])
        cursor.execute(sql % data)
        connect.commit()
    print('TB'+dm_insert_sh_list[q][:6],'收盘价数据获取完成')
    
    #获取市值
    for u in range(len(date_new_list)):
        df_volandincome = jq.get_fundamentals(jq.query(
        jq.valuation.code, 
        jq.valuation.circulating_market_cap, 
        jq.valuation.pe_ratio, 
        jq.income.total_operating_revenue,
        jq.income.np_parent_company_owners 
        ).filter(
        jq.valuation.code == dm_insert_sh_list[q]
        ), date=date_new_list[u])
        volandincome_list=df_volandincome.values.tolist() 
        sql = "update %s set dm='%s' , ltsz=%.2f ,  syl=%.2f  ,  ys=%.2f  ,  jlr=%.2f  where date='%s'"
        try:
            data=('TB'+volandincome_list[0][0][:6],volandincome_list[0][0][:6],volandincome_list[0][1],volandincome_list[0][2],volandincome_list[0][3],volandincome_list[0][4],date_new_list[u])
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()  # 事务回滚
            continue
        else:
            connect.commit()  # 事务提交
    print('TB'+dm_insert_sh_list[q][:6],'市值数据获取完成')
    
    
    #获取资金流向
    zjl_df=jq.get_money_flow(dm_insert_sh_list[q], start_date='2015-01-01', end_date=d, fields=['date','change_pct','net_amount_xl','net_amount_l','net_amount_m','net_amount_s'])
    zjl_list=zjl_df.values.tolist()
    for p in range(0,len(zjl_list)):
        sql = "update %s set zdf=%.2f , cdd=%.2f ,  dd=%.2f  ,  zd=%.2f  ,  xd=%.2f  where date='%s'"
        data=('TB'+dm_cq_list[q],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],zjl_list[p][5],datetime.date(datetime.fromtimestamp(zjl_list[p][0].timestamp())))
        cursor.execute(sql % data)
        connect.commit()  # 事务提交
    print('TB'+dm_insert_sh_list[q][:6],'资金流数据获取完成')
    
    
    
    #获取流通股东   
    date_int_list=[]
    sql2 = "SELECT date FROM rqb order by id "
    cursor.execute(sql2)
    for row in cursor.fetchall():
        p=int(row[0].replace('-','').replace('\'', ''))        
        date_int_list.append(p) 
    for x in range(len(rq_list)): 
        ltgd_df=finance.run_query(jq.query(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.shareholder_rank,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.share_ratio
        ).filter(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code==dm_insert_sh_list[q],
        finance.STK_SHAREHOLDER_FLOATING_TOP10.end_date==rq_list[x]  
        ))
        for z in range(len(date_new_list)):
            if date_int_list[z]>rq_int_list[x] and date_int_list[z]<=rq_int_list[x+1]:
                sql = "  update %s set lt_1=%.2f , lt_2=%.2f  ,lt_3=%.2f  ,lt_4=%.2f  ,lt_5=%.2f  ,lt_6=%.2f  ,lt_7=%.2f  ,lt_8=%.2f  ,lt_9=%.2f  ,lt_10=%.2f    where date='%s'"
                try:
                    data=('TB'+dm_cq_list[q],ltgd_df.iloc[0]['share_ratio'],ltgd_df.iloc[1]['share_ratio'],ltgd_df.iloc[2]['share_ratio'],ltgd_df.iloc[3]['share_ratio'],ltgd_df.iloc[4]['share_ratio'],ltgd_df.iloc[5]['share_ratio'],ltgd_df.iloc[6]['share_ratio'],ltgd_df.iloc[7]['share_ratio'],ltgd_df.iloc[8]['share_ratio'],ltgd_df.iloc[9]['share_ratio'],date_new_list[z])
                    cursor.execute(sql % data)
                except Exception as e:
                    connect.rollback()  # 事务回滚
                else:
                    connect.commit()  # 事务提交
    print('TB'+dm_insert_sh_list[q][:6],'流通股东数据获取完成')  
print('除权所有数据插入完毕....................................')   
print(d,'除权完成***********************************************')  




# 关闭连接
cursor.close()
connect.close()