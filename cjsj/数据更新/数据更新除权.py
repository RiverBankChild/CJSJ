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



#----------------------------------------------------数据更新
#判断是否为节假日或者工作日六点以后
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print('今天是'+d)
start_time = dt.datetime.strptime(str(dt.datetime.now().date())+'18:00', '%Y-%m-%d%H:%M')
n_time = dt.datetime.now()
if chinese_calendar.is_holiday(n_time):
    pass
else:
    if n_time > start_time:
        pass
    else:
        print('当前时间段不允许更新数据')
        os._exit(0)

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

#获取现有代码表
dm_old_list=[]
sql = "SELECT dm ,name FROM dmb order by id "
cursor.execute(sql)
for a in cursor.fetchall():
    dm_old_list.append(list(a))     
    
#获取现有日期表
date_old_list=[]
sql = "SELECT date FROM rqb order by id "
cursor.execute(sql)
for b in cursor.fetchall():
    date_old_list.append(b[0]) 


#获取最新代码表
dm_new_list=[]
df_new=jq.get_all_securities(date=d );
df_new.drop(columns=['start_date', 'end_date','type','name'],axis=1,inplace=True);
df_new.rename(columns={'display_name':'name'},inplace=True)
df_new.reset_index(inplace=True,drop=False)
df_new.rename(columns={'index':'dm'},inplace=True)
for i in range(0, len(df_new)):
    df_new.iloc[i]['dm']=df_new.iloc[i]['dm'][:6] 
dm_new_list=df_new.values.tolist()  



#更新上证指数 
szzs_df=jq.get_price('000001.XSHG',  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
szzs_df.reset_index(inplace=True,drop=False)
szzs_list=szzs_df.values.tolist()
total=0;
sql10="truncate table szzs"
cursor.execute(sql10)
connect.commit() 
for j in range(len(szzs_list)):
    try:
        sql = "INSERT INTO szzs (date,open,close,high,low,volume) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )"
        date = datetime.date(datetime.fromtimestamp(szzs_list[j][0].timestamp()))        
        data = (date,szzs_list[j][1],szzs_list[j][2],szzs_list[j][3],szzs_list[j][4],szzs_list[j][5])
        cursor.execute(sql % data)
    except Exception as e:
        connect.rollback()  # 事务回滚
        continue
    else:
        connect.commit()  # 事务提交
        total=total+cursor.rowcount
print('上证指数历史数据更新完成，共更新了',total,'条数据')


#更新日期表
total=0;
date_list=[]
sql = "SELECT date FROM szzs order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    date_list.append(row)
    
sql11="truncate table rqb"
cursor.execute(sql11)
connect.commit() 
   
for k in range(0,len(date_list)):
    try:
        sql = "INSERT INTO rqb (date) VALUES ( '%s')"
        datek =date_list[k]         
        datak = (datek)
        cursor.execute(sql % datak)
    except Exception as e:
        connect.rollback()  # 事务回滚
        continue
    else:
        connect.commit()  # 事务提交
        total=total+cursor.rowcount
print('日期表更新完成，共更新了',total,'条数据')

#获取最新日期表
date_new_list=[]
sql = "SELECT date FROM rqb order by id "
cursor.execute(sql)
for c in cursor.fetchall():
    date_new_list.append(c[0]) 



#获取报告期数据
rq_list=['2019-03-31','2019-06-30','2019-09-30','2019-12-31','2020-03-31','2020-06-30','2020-09-30','2020-12-31']
rq_int_list=[20190331,20190630,20190930,20191231,20200331,20200630,20200930,20201231]
    
#对比新老代码表和日期表

date_insert_list=[]
dm_insert_list=[]
dm_delete_list=[]
dm_update_list=[]
dm_old_int_list=[]
dm_new_int_list=[]

for a0 in range(len(dm_old_list)):
    dm_old_int_list.append(dm_old_list[a0][0])
for b0 in range(len(dm_new_list)):
    dm_new_int_list.append(dm_new_list[b0][0])
    
for f in range(len(date_new_list)):
    if date_new_list[f] in date_old_list:
        pass
    else:
        date_insert_list.append(date_new_list[f])
        
for g in range(len(dm_new_list)):
    if dm_new_int_list[g] in dm_old_int_list:
        pass
    else:
        dm_insert_list.append(dm_new_list[g])
        
for h in range(len(dm_old_list)):
    if dm_old_int_list[h] in dm_new_int_list:
        pass
    else:
        dm_delete_list.append(dm_old_list[h])

for ee in range(len(dm_old_list)):
    if dm_old_list[ee] in dm_delete_list:
        pass
    else:
        dm_update_list.append(dm_old_list[ee])
print('需要更新的日期：',date_insert_list)       
print('新上市：',dm_insert_list)
print('退市：',dm_delete_list)
    

#更新代码表
total=0
for m in range(len(dm_insert_list)):
    sql = "INSERT INTO dmb (dm,name) VALUES ( '%s', '%s')"
    data = (dm_insert_list[m][0],dm_insert_list[m][1])
    cursor.execute(sql % data)
    connect.commit()
    total=total+cursor.rowcount
print('成功插入代码表', total, '支股票')

total=0
for n in range(len(dm_delete_list)):
    sql = "delete from dmb where dm='%s'"
    data = (dm_delete_list[n][0])
    cursor.execute(sql % data)
    connect.commit()
    total=total+cursor.rowcount
print('成功删除代码表', total, '支股票')

total=0
for n in range(len(dm_delete_list)):
    sql = "delete from kxfzb where dm='%s'"
    data = (dm_delete_list[n][0])
    cursor.execute(sql % data)
    connect.commit()
    total=total+cursor.rowcount
print('成功删除可选分组表', total, '支股票')


#更新股票表  
#1.删除停止上市的表

for o in range(len(dm_delete_list)):
    sql = " drop table %s "
    data = ('TB'+dm_delete_list[o][0])
    cursor.execute(sql%data)
    connect.commit()
    print('成功删除', 'TB'+dm_delete_list[o][0])


#2.插入新上市的表

for p in range(0, len(dm_insert_list)):
    sql = "create table IF NOT EXISTS %s (\
    id int primary key auto_increment,\
    dm varchar(8)  default '未知代码',\
    date varchar(16) unique default '未知日期',\
    open Float(7,2) default  0.00,\
    close Float(7,2) default  0.00,\
    high Float(7,2) default  0.00,\
    low Float(7,2) default  0.00,\
    zdf  Float(5,2) default  0.00,\
    cjl Float(14,2) default  0.00,\
    ltsz   Float(14,2) default  0.00,\
    syl    Float(10,2)  default  0.00,\
    ys     Float(14,2) default  0.00,\
    jlr    Float(14,2) default  0.00,\
    cdd    Float(14,2) default  0.00,\
    dd    Float(14,2) default  0.00,\
    zd    Float(14,2) default  0.00,\
    xd    Float(14,2) default  0.00,\
    lt_1  Float(5,2) default  0.00,\
    lt_2  Float(5,2) default  0.00,\
    lt_3  Float(5,2) default  0.00,\
    lt_4  Float(5,2) default  0.00,\
    lt_5  Float(5,2) default  0.00,\
    lt_6  Float(5,2) default  0.00,\
    lt_7  Float(5,2) default  0.00,\
    lt_8  Float(5,2) default  0.00,\
    lt_9  Float(5,2) default  0.00,\
    lt_10  Float(5,2) default  0.00\
    );"       
    data = ('TB'+dm_insert_list[p][0])
    cursor.execute(sql % data)
    connect.commit()
    print('成功创建','TB'+dm_insert_list[p][0])

#3.向新增加的表中插入数据
print("开始向新上市的表中插入数据...................................................")
dm_insert_sh_list=[]
for s in range(len(dm_insert_list)):
    if dm_insert_list[s][0].startswith('6'):
        t=dm_insert_list[s][0]+'.XSHG'
    else:
        t=dm_insert_list[s][0]+'.XSHE'        
    dm_insert_sh_list.append(t)
for q in range(0, len(dm_insert_list)):
    #获取收盘价
    insert_df=jq.get_price(dm_insert_sh_list[q],  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
    insert_df.reset_index(inplace=True,drop=False)
    insert_list=insert_df.values.tolist()
    for s in range(len(insert_list)):
        sql = "INSERT INTO %s (date,open,close,high,low,cjl) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )" 
        date = datetime.date(datetime.fromtimestamp(insert_list[s][0].timestamp()))       
        data = ('TB'+dm_insert_list[q][0],date,insert_list[s][1],insert_list[s][2],insert_list[s][3],insert_list[s][4],insert_list[s][5])
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
        data=('TB'+dm_insert_list[q][0],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],zjl_list[p][5],datetime.date(datetime.fromtimestamp(zjl_list[p][0].timestamp())))
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
                    data=('TB'+dm_insert_list[q][0],ltgd_df.iloc[0]['share_ratio'],ltgd_df.iloc[1]['share_ratio'],ltgd_df.iloc[2]['share_ratio'],ltgd_df.iloc[3]['share_ratio'],ltgd_df.iloc[4]['share_ratio'],ltgd_df.iloc[5]['share_ratio'],ltgd_df.iloc[6]['share_ratio'],ltgd_df.iloc[7]['share_ratio'],ltgd_df.iloc[8]['share_ratio'],ltgd_df.iloc[9]['share_ratio'],date_new_list[z])
                    cursor.execute(sql % data)
                except Exception as e:
                    connect.rollback()  # 事务回滚
                else:
                    connect.commit()  # 事务提交
    print('TB'+dm_insert_sh_list[q][:6],'流通股东数据获取完成')  
print('新表所有数据插入完毕....................................')   


#更新老表数据
print("开始向老表更新数据...................................")
dm_sh_list=[]
for at in range(len(dm_update_list)):
    if dm_update_list[at][0].startswith('6'):
        th=dm_update_list[at][0]+'.XSHG'
    else:
        th=dm_update_list[at][0]+'.XSHE'        
    dm_sh_list.append(th)
for q in range(0, len(dm_update_list)):
    #更新收盘价
    total_df=jq.get_price(dm_sh_list[q],start_date=date_insert_list[0] , end_date=date_insert_list[-1], frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
    total_df.reset_index(inplace=True,drop=False)
    total_list=total_df.values.tolist()
    for s in range(0,len(total_list)):
        sql = " INSERT INTO %s (date,open,close,high,low,cjl) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )" 
        try:
            date = datetime.date(datetime.fromtimestamp(total_list[s][0].timestamp()))       
            data = ('TB'+dm_update_list[q][0],date,total_list[s][1],total_list[s][2],total_list[s][3],total_list[s][4],total_list[s][5])
            cursor.execute(sql % data) 
        except Exception as e:
            connect.rollback()  # 事务回滚
            continue
        else:
            connect.commit()  # 事务提交
    
    #更新市值
    for u in range(0,len(date_insert_list)):
        df_total_volandincome = jq.get_fundamentals(jq.query(
        jq.valuation.code, 
        jq.valuation.circulating_market_cap, 
        jq.valuation.pe_ratio, 
        jq.income.total_operating_revenue,
        jq.income.np_parent_company_owners 
        ).filter(
        jq.valuation.code == dm_sh_list[q]
        ), date=date_insert_list[u])
        volandincome_list=df_total_volandincome.values.tolist()
        sql = "update %s set dm='%s' , ltsz=%.2f ,  syl=%.2f  ,  ys=%.2f  ,  jlr=%.2f  where date='%s'"
        try:
            data=('TB'+volandincome_list[0][0][:6],volandincome_list[0][0][:6],volandincome_list[0][1],volandincome_list[0][2],volandincome_list[0][3],volandincome_list[0][4],date_insert_list[u])
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()  # 事务回滚
            continue
        else:
            connect.commit()  # 事务提交

    
    #更新资金流向
    zjl_df=jq.get_money_flow(dm_sh_list[q], start_date=date_insert_list[0] , end_date=date_insert_list[-1], fields=['date','change_pct','net_amount_xl','net_amount_l','net_amount_m','net_amount_s'])
    zjl_list=zjl_df.values.tolist()
    for p in range(0,len(zjl_list)):
        sql = "update %s set zdf=%.2f, cdd=%.2f ,  dd=%.2f  ,  zd=%.2f  ,  xd=%.2f  where date='%s'"
        try:
            data=('TB'+dm_update_list[q][0],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],zjl_list[p][5],datetime.date(datetime.fromtimestamp(zjl_list[p][0].timestamp())))
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()  # 事务回滚
            continue
        else:
            connect.commit()  # 事务提交
        
    #获取流通股东   
    date_insert_int_list=[]
    for row in range(0,len(date_insert_list)):
        p=int(date_insert_list[row].replace('-','').replace('\'', ''))        
        date_insert_int_list.append(p) 
    for x in range(len(rq_list)): 
        ltgd_df=finance.run_query(jq.query(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.shareholder_rank,
        finance.STK_SHAREHOLDER_FLOATING_TOP10.share_ratio
        ).filter(
        finance.STK_SHAREHOLDER_FLOATING_TOP10.code==dm_sh_list[q],
        finance.STK_SHAREHOLDER_FLOATING_TOP10.end_date==rq_list[x]  
        ))
        for z in range(len(date_insert_list)):
            if date_insert_int_list[z]>rq_int_list[x] and date_insert_int_list[z]<=rq_int_list[x+1]:
                sql = "  update %s set lt_1=%.2f , lt_2=%.2f  ,lt_3=%.2f  ,lt_4=%.2f  ,lt_5=%.2f  ,lt_6=%.2f  ,lt_7=%.2f  ,lt_8=%.2f  ,lt_9=%.2f  ,lt_10=%.2f    where date='%s'"
                try:
                    data=('TB'+dm_update_list[q][0],ltgd_df.iloc[0]['share_ratio'],ltgd_df.iloc[1]['share_ratio'],ltgd_df.iloc[2]['share_ratio'],ltgd_df.iloc[3]['share_ratio'],ltgd_df.iloc[4]['share_ratio'],ltgd_df.iloc[5]['share_ratio'],ltgd_df.iloc[6]['share_ratio'],ltgd_df.iloc[7]['share_ratio'],ltgd_df.iloc[8]['share_ratio'],ltgd_df.iloc[9]['share_ratio'],date_insert_list[z])
                    cursor.execute(sql % data)
                except Exception as e:
                    connect.rollback()  # 事务回滚
                    continue
                else:
                    connect.commit()  # 事务提交
            else:
                pass
    print('TB'+dm_sh_list[q][:6],'数据更新完成')  
print('所有表所有数据更新完毕....................................') 


  




#----------------------------------------------------数据除权


print("...............开始修正除权数据..............................")


#定义编码方法
def js(open,high,low,close):   
    d=0
    x=0
    if(open>=close):
        d=open
        x=close
    if(open<close):
        d=close
        x=open
    
    h=high-d
    l=x-low
       
    return h,l


#openzl=[[-10.6,-9.94],[-9.94,-7],[-7,-3],[-3,-1],[-1,1],[1,3],[3,7],[7,9.94],[9.94,10.6]]
#closezl=[[-10.6,-9.94],[-9.94,-7],[-7,-4],[-4,-2],[-2,-1],[-1,0],[0,1],[1,2],[2,4],[4,7],[7,9.94],[9.94,10.6]]
#normzl=[[0,1.5],[1.5,3.5],[3.5,20.5]]


def bm(open,high,low,close):
    num=0
    if(open>=-10.6 and open<=-9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=1
            if(h>=1.5 and h<3.5):
                num=2
            if(h>=3.5 and h<=20.5):
                num=3
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=4
            if(h>=1.5 and h<3.5):
                num=5
            if(h>=3.5 and h<=20.5):
                num=6
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=7
            if(h>=1.5 and h<3.5):
                num=8
            if(h>=3.5 and h<=20.5):
                num=9
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=10
            if(h>=1.5 and h<3.5):
                num=11
            if(h>=3.5 and h<=20.5):
                num=12
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=13
            if(h>=1.5 and h<3.5):
                num=14
            if(h>=3.5 and h<=20.5):
                num=15
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=16
            if(h>=1.5 and h<3.5):
                num=17
            if(h>=3.5 and h<=20.5):
                num=18
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=19
            if(h>=1.5 and h<3.5):
                num=20
            if(h>=3.5 and h<=20.5):
                num=21
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=22
            if(h>=1.5 and h<3.5):
                num=23
            if(h>=3.5 and h<=20.5):
                num=24
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=25
            if(h>=1.5 and h<3.5):
                num=26
            if(h>=3.5 and h<=20.5):
                num=27
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=28
            if(h>=1.5 and h<3.5):
                num=29
            if(h>=3.5 and h<=20.5):
                num=30
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=31
            if(h>=1.5 and h<3.5):
                num=32
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            num=33





    if(open>-9.94 and open<-7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=34
            if(h>=1.5 and h<3.5):
                num=35
            if(h>=3.5 and h<=20.5):
                num=36
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=37
                if(l>=1.5 and l<3.5):
                    num=38
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=39
                if(l>=1.5 and l<3.5):
                    num=40
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=41
                if(l>=1.5 and l<3.5):
                    num=42
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=43
                if(l>=1.5 and l<3.5):
                    num=44
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=45
                if(l>=1.5 and l<3.5):
                    num=46
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=47
                if(l>=1.5 and l<3.5):
                    num=48
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=49
                if(l>=1.5 and l<3.5):
                    num=50
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=51
                if(l>=1.5 and l<3.5):
                    num=52
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=53
                if(l>=1.5 and l<3.5):
                    num=54
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=55
                if(l>=1.5 and l<3.5):
                    num=56
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=57
                if(l>=1.5 and l<3.5):
                    num=58
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=59
                if(l>=1.5 and l<3.5):
                    num=60
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=61
                if(l>=1.5 and l<3.5):
                    num=62
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=63
                if(l>=1.5 and l<3.5):
                    num=64
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=65
                if(l>=1.5 and l<3.5):
                    num=66
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=67
                if(l>=1.5 and l<3.5):
                    num=68
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=69
                if(l>=1.5 and l<3.5):
                    num=70
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=71
                if(l>=1.5 and l<3.5):
                    num=72
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=73
                if(l>=1.5 and l<3.5):
                    num=74
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=75
                if(l>=1.5 and l<3.5):
                    num=76
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=77
                if(l>=1.5 and l<3.5):
                    num=78
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=79
                if(l>=1.5 and l<3.5):
                    num=80
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=81
                if(l>=1.5 and l<3.5):
                    num=82
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=83
                if(l>=1.5 and l<3.5):
                    num=84
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=85
                if(l>=1.5 and l<3.5):
                    num=86
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=87
                if(l>=1.5 and l<3.5):
                    num=88
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=89
                if(l>=1.5 and l<3.5):
                    num=90
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=91
                if(l>=1.5 and l<3.5):
                    num=92
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=93
                if(l>=1.5 and l<3.5):
                    num=94
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=95
            if(l>=1.5 and l<3.5):
                num=96



    if(open>=-7 and open<-3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=97
            if(h>=1.5 and h<3.5):
                num=98
            if(h>=3.5 and h<=20.5):
                num=99
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=100
                if(l>=1.5 and l<3.5):
                    num=101
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=102
                if(l>=1.5 and l<3.5):
                    num=103
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=104
                if(l>=1.5 and l<3.5):
                    num=105
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=106
                if(l>=1.5 and l<3.5):
                    num=107
                if(l>=3.5 and l<20.5):
                    num=108
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=109
                if(l>=1.5 and l<3.5):
                    num=110
                if(l>=3.5 and l<20.5):
                    num=111
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=112
                if(l>=1.5 and l<3.5):
                    num=113
                if(l>=3.5 and l<20.5):
                    num=114
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=115
                if(l>=1.5 and l<3.5):
                    num=116
                if(l>=3.5 and l<=20.5):
                    num=117
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=118
                if(l>=1.5 and l<3.5):
                    num=119
                if(l>=3.5 and l<=20.5):
                    num=120
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=121
                if(l>=1.5 and l<3.5):
                    num=122
                if(l>=3.5 and l<=20.5):
                    num=123
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=124
                if(l>=1.5 and l<3.5):
                    num=125
                if(l>=3.5 and l<=20.5):
                    num=126
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=127
                if(l>=1.5 and l<3.5):
                    num=128
                if(l>=3.5 and l<=20.5):
                    num=129
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=130
                if(l>=1.5 and l<3.5):
                    num=131
                if(l>=3.5 and l<=20.5):
                    num=132
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=133
                if(l>=1.5 and l<3.5):
                    num=134
                if(l>=3.5 and l<=20.5):
                    num=135
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=136
                if(l>=1.5 and l<3.5):
                    num=137
                if(l>=3.5 and l<=20.5):
                    num=138
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=139
                if(l>=1.5 and l<3.5):
                    num=140
                if(l>=3.5 and l<=20.5):
                    num=141
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=142
                if(l>=1.5 and l<3.5):
                    num=143
                if(l>=3.5 and l<=20.5):
                    num=144
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=145
                if(l>=1.5 and l<3.5):
                    num=146
                if(l>=3.5 and l<=20.5):
                    num=147
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=148
                if(l>=1.5 and l<3.5):
                    num=149
                if(l>=3.5 and l<=20.5):
                    num=150
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=151
                if(l>=1.5 and l<3.5):
                    num=152
                if(l>=3.5 and l<=20.5):
                    num=153
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=154
                if(l>=1.5 and l<3.5):
                    num=155
                if(l>=3.5 and l<=20.5):
                    num=156
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=157
                if(l>=1.5 and l<3.5):
                    num=158
                if(l>=3.5 and l<=20.5):
                    num=159
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=160
                if(l>=1.5 and l<3.5):
                    num=161
                if(l>=3.5 and l<=20.5):
                    num=162
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=163
                if(l>=1.5 and l<3.5):
                    num=164
                if(l>=3.5 and l<=20.5):
                    num=165
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=166
                if(l>=1.5 and l<3.5):
                    num=167
                if(l>=3.5 and l<=20.5):
                    num=168
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=169
                if(l>=1.5 and l<3.5):
                    num=170
                if(l>=3.5 and l<=20.5):
                    num=171
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=172
                if(l>=1.5 and l<3.5):
                    num=173
                if(l>=3.5 and l<=20.5):
                    num=174
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=175
                if(l>=1.5 and l<3.5):
                    num=176
                if(l>=3.5 and l<=20.5):
                    num=177
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=178
                if(l>=1.5 and l<3.5):
                    num=179
                if(l>=3.5 and l<=20.5):
                    num=180
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=181
                if(l>=1.5 and l<3.5):
                    num=182
                if(l>=3.5 and l<=20.5):
                    num=183
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=184
            if(l>=1.5 and l<3.5):
                num=185
            if(l>=3.5 and l<=20.5):
                num=186




    if(open>=-3 and open<-1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=187
            if(h>=1.5 and h<3.5):
                num=188
            if(h>=3.5 and h<=20.5):
                num=189
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=190
                if(l>=1.5 and l<3.5):
                    num=191
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=192
                if(l>=1.5 and l<3.5):
                    num=193
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=194
                if(l>=1.5 and l<3.5):
                    num=195
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=196
                if(l>=1.5 and l<3.5):
                    num=197
                if(l>=3.5 and l<20.5):
                    num=198
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=199
                if(l>=1.5 and l<3.5):
                    num=200
                if(l>=3.5 and l<20.5):
                    num=201
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=202
                if(l>=1.5 and l<3.5):
                    num=203
                if(l>=3.5 and l<20.5):
                    num=204
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=205
                if(l>=1.5 and l<3.5):
                    num=206
                if(l>=3.5 and l<=20.5):
                    num=207
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=208
                if(l>=1.5 and l<3.5):
                    num=209
                if(l>=3.5 and l<=20.5):
                    num=210
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=211
                if(l>=1.5 and l<3.5):
                    num=212
                if(l>=3.5 and l<=20.5):
                    num=213
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=214
                if(l>=1.5 and l<3.5):
                    num=215
                if(l>=3.5 and l<=20.5):
                    num=216
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=217
                if(l>=1.5 and l<3.5):
                    num=218
                if(l>=3.5 and l<=20.5):
                    num=219
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=220
                if(l>=1.5 and l<3.5):
                    num=221
                if(l>=3.5 and l<=20.5):
                    num=222
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=223
                if(l>=1.5 and l<3.5):
                    num=224
                if(l>=3.5 and l<=20.5):
                    num=225
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=226
                if(l>=1.5 and l<3.5):
                    num=227
                if(l>=3.5 and l<=20.5):
                    num=228
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=229
                if(l>=1.5 and l<3.5):
                    num=230
                if(l>=3.5 and l<=20.5):
                    num=231
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=232
                if(l>=1.5 and l<3.5):
                    num=233
                if(l>=3.5 and l<=20.5):
                    num=234
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=235
                if(l>=1.5 and l<3.5):
                    num=236
                if(l>=3.5 and l<=20.5):
                    num=237
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=238
                if(l>=1.5 and l<3.5):
                    num=239
                if(l>=3.5 and l<=20.5):
                    num=240
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=241
                if(l>=1.5 and l<3.5):
                    num=242
                if(l>=3.5 and l<=20.5):
                    num=243
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=244
                if(l>=1.5 and l<3.5):
                    num=245
                if(l>=3.5 and l<=20.5):
                    num=246
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=247
                if(l>=1.5 and l<3.5):
                    num=248
                if(l>=3.5 and l<=20.5):
                    num=249
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=250
                if(l>=1.5 and l<3.5):
                    num=251
                if(l>=3.5 and l<=20.5):
                    num=252
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=253
                if(l>=1.5 and l<3.5):
                    num=254
                if(l>=3.5 and l<=20.5):
                    num=255
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=256
                if(l>=1.5 and l<3.5):
                    num=257
                if(l>=3.5 and l<=20.5):
                    num=258
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=259
                if(l>=1.5 and l<3.5):
                    num=260
                if(l>=3.5 and l<=20.5):
                    num=261
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=262
                if(l>=1.5 and l<3.5):
                    num=263
                if(l>=3.5 and l<=20.5):
                    num=264
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=265
                if(l>=1.5 and l<3.5):
                    num=266
                if(l>=3.5 and l<=20.5):
                    num=267
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=268
                if(l>=1.5 and l<3.5):
                    num=269
                if(l>=3.5 and l<=20.5):
                    num=270
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=271
                if(l>=1.5 and l<3.5):
                    num=272
                if(l>=3.5 and l<=20.5):
                    num=273
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=274
            if(l>=1.5 and l<3.5):
                num=275
            if(l>=3.5 and l<=20.5):
                num=276



    if(open>=-1 and open<1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=277
            if(h>=1.5 and h<3.5):
                num=278
            if(h>=3.5 and h<=20.5):
                num=279
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=280
                if(l>=1.5 and l<3.5):
                    num=281
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=282
                if(l>=1.5 and l<3.5):
                    num=283
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=284
                if(l>=1.5 and l<3.5):
                    num=285
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=286
                if(l>=1.5 and l<3.5):
                    num=287
                if(l>=3.5 and l<20.5):
                    num=288
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=289
                if(l>=1.5 and l<3.5):
                    num=290
                if(l>=3.5 and l<20.5):
                    num=291
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=292
                if(l>=1.5 and l<3.5):
                    num=293
                if(l>=3.5 and l<20.5):
                    num=294
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=295
                if(l>=1.5 and l<3.5):
                    num=296
                if(l>=3.5 and l<=20.5):
                    num=297
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=298
                if(l>=1.5 and l<3.5):
                    num=299
                if(l>=3.5 and l<=20.5):
                    num=300
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=301
                if(l>=1.5 and l<3.5):
                    num=302
                if(l>=3.5 and l<=20.5):
                    num=303
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=304
                if(l>=1.5 and l<3.5):
                    num=305
                if(l>=3.5 and l<=20.5):
                    num=306
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=307
                if(l>=1.5 and l<3.5):
                    num=308
                if(l>=3.5 and l<=20.5):
                    num=309
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=310
                if(l>=1.5 and l<3.5):
                    num=311
                if(l>=3.5 and l<=20.5):
                    num=312
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=313
                if(l>=1.5 and l<3.5):
                    num=314
                if(l>=3.5 and l<=20.5):
                    num=315
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=316
                if(l>=1.5 and l<3.5):
                    num=317
                if(l>=3.5 and l<=20.5):
                    num=318
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=319
                if(l>=1.5 and l<3.5):
                    num=320
                if(l>=3.5 and l<=20.5):
                    num=321
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=322
                if(l>=1.5 and l<3.5):
                    num=323
                if(l>=3.5 and l<=20.5):
                    num=324
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=325
                if(l>=1.5 and l<3.5):
                    num=326
                if(l>=3.5 and l<=20.5):
                    num=327
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=328
                if(l>=1.5 and l<3.5):
                    num=329
                if(l>=3.5 and l<=20.5):
                    num=330
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=331
                if(l>=1.5 and l<3.5):
                    num=332
                if(l>=3.5 and l<=20.5):
                    num=333
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=334
                if(l>=1.5 and l<3.5):
                    num=335
                if(l>=3.5 and l<=20.5):
                    num=336
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=337
                if(l>=1.5 and l<3.5):
                    num=338
                if(l>=3.5 and l<=20.5):
                    num=339
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=340
                if(l>=1.5 and l<3.5):
                    num=341
                if(l>=3.5 and l<=20.5):
                    num=342
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=343
                if(l>=1.5 and l<3.5):
                    num=344
                if(l>=3.5 and l<=20.5):
                    num=345
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=346
                if(l>=1.5 and l<3.5):
                    num=347
                if(l>=3.5 and l<=20.5):
                    num=348
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=349
                if(l>=1.5 and l<3.5):
                    num=350
                if(l>=3.5 and l<=20.5):
                    num=351
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=352
                if(l>=1.5 and l<3.5):
                    num=353
                if(l>=3.5 and l<=20.5):
                    num=354
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=355
                if(l>=1.5 and l<3.5):
                    num=356
                if(l>=3.5 and l<=20.5):
                    num=357
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=358
                if(l>=1.5 and l<3.5):
                    num=359
                if(l>=3.5 and l<=20.5):
                    num=360
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=361
                if(l>=1.5 and l<3.5):
                    num=362
                if(l>=3.5 and l<=20.5):
                    num=363
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=364
            if(l>=1.5 and l<3.5):
                num=365
            if(l>=3.5 and l<=20.5):
                num=366


    if(open>=1 and open<3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=367
            if(h>=1.5 and h<3.5):
                num=368
            if(h>=3.5 and h<=20.5):
                num=369
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=370
                if(l>=1.5 and l<3.5):
                    num=371
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=372
                if(l>=1.5 and l<3.5):
                    num=373
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=374
                if(l>=1.5 and l<3.5):
                    num=375
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=376
                if(l>=1.5 and l<3.5):
                    num=377
                if(l>=3.5 and l<20.5):
                    num=378
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=379
                if(l>=1.5 and l<3.5):
                    num=380
                if(l>=3.5 and l<20.5):
                    num=381
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=382
                if(l>=1.5 and l<3.5):
                    num=383
                if(l>=3.5 and l<20.5):
                    num=384
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=385
                if(l>=1.5 and l<3.5):
                    num=386
                if(l>=3.5 and l<=20.5):
                    num=387
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=388
                if(l>=1.5 and l<3.5):
                    num=389
                if(l>=3.5 and l<=20.5):
                    num=390
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=391
                if(l>=1.5 and l<3.5):
                    num=392
                if(l>=3.5 and l<=20.5):
                    num=393
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=394
                if(l>=1.5 and l<3.5):
                    num=395
                if(l>=3.5 and l<=20.5):
                    num=396
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=397
                if(l>=1.5 and l<3.5):
                    num=398
                if(l>=3.5 and l<=20.5):
                    num=399
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=400
                if(l>=1.5 and l<3.5):
                    num=401
                if(l>=3.5 and l<=20.5):
                    num=402
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=403
                if(l>=1.5 and l<3.5):
                    num=404
                if(l>=3.5 and l<=20.5):
                    num=405
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=406
                if(l>=1.5 and l<3.5):
                    num=407
                if(l>=3.5 and l<=20.5):
                    num=408
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=409
                if(l>=1.5 and l<3.5):
                    num=410
                if(l>=3.5 and l<=20.5):
                    num=411
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=412
                if(l>=1.5 and l<3.5):
                    num=413
                if(l>=3.5 and l<=20.5):
                    num=414
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=415
                if(l>=1.5 and l<3.5):
                    num=416
                if(l>=3.5 and l<=20.5):
                    num=417
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=418
                if(l>=1.5 and l<3.5):
                    num=419
                if(l>=3.5 and l<=20.5):
                    num=420
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=421
                if(l>=1.5 and l<3.5):
                    num=422
                if(l>=3.5 and l<=20.5):
                    num=423
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=424
                if(l>=1.5 and l<3.5):
                    num=425
                if(l>=3.5 and l<=20.5):
                    num=426
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=427
                if(l>=1.5 and l<3.5):
                    num=428
                if(l>=3.5 and l<=20.5):
                    num=429
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=430
                if(l>=1.5 and l<3.5):
                    num=431
                if(l>=3.5 and l<=20.5):
                    num=432
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=433
                if(l>=1.5 and l<3.5):
                    num=434
                if(l>=3.5 and l<=20.5):
                    num=435
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=436
                if(l>=1.5 and l<3.5):
                    num=437
                if(l>=3.5 and l<=20.5):
                    num=438
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=439
                if(l>=1.5 and l<3.5):
                    num=440
                if(l>=3.5 and l<=20.5):
                    num=441
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=442
                if(l>=1.5 and l<3.5):
                    num=443
                if(l>=3.5 and l<=20.5):
                    num=444
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=445
                if(l>=1.5 and l<3.5):
                    num=446
                if(l>=3.5 and l<=20.5):
                    num=447
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=448
                if(l>=1.5 and l<3.5):
                    num=449
                if(l>=3.5 and l<=20.5):
                    num=450
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=451
                if(l>=1.5 and l<3.5):
                    num=452
                if(l>=3.5 and l<=20.5):
                    num=453
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=454
            if(l>=1.5 and l<3.5):
                num=455
            if(l>=3.5 and l<=20.5):
                num=456




    if(open>=3 and open<7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=457
            if(h>=1.5 and h<3.5):
                num=458
            if(h>=3.5 and h<=20.5):
                num=459
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=460
                if(l>=1.5 and l<3.5):
                    num=461
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=462
                if(l>=1.5 and l<3.5):
                    num=463
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=464
                if(l>=1.5 and l<3.5):
                    num=465
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=466
                if(l>=1.5 and l<3.5):
                    num=467
                if(l>=3.5 and l<20.5):
                    num=468
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=469
                if(l>=1.5 and l<3.5):
                    num=470
                if(l>=3.5 and l<20.5):
                    num=471
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=472
                if(l>=1.5 and l<3.5):
                    num=473
                if(l>=3.5 and l<20.5):
                    num=474
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=475
                if(l>=1.5 and l<3.5):
                    num=476
                if(l>=3.5 and l<=20.5):
                    num=477
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=478
                if(l>=1.5 and l<3.5):
                    num=479
                if(l>=3.5 and l<=20.5):
                    num=480
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=481
                if(l>=1.5 and l<3.5):
                    num=482
                if(l>=3.5 and l<=20.5):
                    num=483
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=484
                if(l>=1.5 and l<3.5):
                    num=485
                if(l>=3.5 and l<=20.5):
                    num=486
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=487
                if(l>=1.5 and l<3.5):
                    num=488
                if(l>=3.5 and l<=20.5):
                    num=489
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=490
                if(l>=1.5 and l<3.5):
                    num=491
                if(l>=3.5 and l<=20.5):
                    num=492
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=493
                if(l>=1.5 and l<3.5):
                    num=494
                if(l>=3.5 and l<=20.5):
                    num=495
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=496
                if(l>=1.5 and l<3.5):
                    num=497
                if(l>=3.5 and l<=20.5):
                    num=498
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=499
                if(l>=1.5 and l<3.5):
                    num=500
                if(l>=3.5 and l<=20.5):
                    num=501
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=502
                if(l>=1.5 and l<3.5):
                    num=503
                if(l>=3.5 and l<=20.5):
                    num=504
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=505
                if(l>=1.5 and l<3.5):
                    num=506
                if(l>=3.5 and l<=20.5):
                    num=507
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=508
                if(l>=1.5 and l<3.5):
                    num=509
                if(l>=3.5 and l<=20.5):
                    num=510
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=511
                if(l>=1.5 and l<3.5):
                    num=512
                if(l>=3.5 and l<=20.5):
                    num=513
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=514
                if(l>=1.5 and l<3.5):
                    num=515
                if(l>=3.5 and l<=20.5):
                    num=516
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=517
                if(l>=1.5 and l<3.5):
                    num=518
                if(l>=3.5 and l<=20.5):
                    num=519
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=520
                if(l>=1.5 and l<3.5):
                    num=521
                if(l>=3.5 and l<=20.5):
                    num=522
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=523
                if(l>=1.5 and l<3.5):
                    num=524
                if(l>=3.5 and l<=20.5):
                    num=525
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=526
                if(l>=1.5 and l<3.5):
                    num=527
                if(l>=3.5 and l<=20.5):
                    num=528
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=529
                if(l>=1.5 and l<3.5):
                    num=530
                if(l>=3.5 and l<=20.5):
                    num=531
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=532
                if(l>=1.5 and l<3.5):
                    num=533
                if(l>=3.5 and l<=20.5):
                    num=534
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=535
                if(l>=1.5 and l<3.5):
                    num=536
                if(l>=3.5 and l<=20.5):
                    num=537
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=538
                if(l>=1.5 and l<3.5):
                    num=539
                if(l>=3.5 and l<=20.5):
                    num=540
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=541
                if(l>=1.5 and l<3.5):
                    num=542
                if(l>=3.5 and l<=20.5):
                    num=543
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=544
            if(l>=1.5 and l<3.5):
                num=545
            if(l>=3.5 and l<=20.5):
                num=546



    if(open>=7 and open<9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=547
            if(h>=1.5 and h<3.5):
                num=548
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=549
                if(l>=1.5 and l<3.5):
                    num=550
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=551
                if(l>=1.5 and l<3.5):
                    num=552
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=553
                if(l>=1.5 and l<3.5):
                    num=554
                if(l>=3.5 and l<20.5):
                    num=555
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=556
                if(l>=1.5 and l<3.5):
                    num=557
                if(l>=3.5 and l<20.5):
                    num=558
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=559
                if(l>=1.5 and l<3.5):
                    num=560
                if(l>=3.5 and l<=20.5):
                    num=561
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=562
                if(l>=1.5 and l<3.5):
                    num=563
                if(l>=3.5 and l<=20.5):
                    num=564
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=565
                if(l>=1.5 and l<3.5):
                    num=566
                if(l>=3.5 and l<=20.5):
                    num=567
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=568
                if(l>=1.5 and l<3.5):
                    num=569
                if(l>=3.5 and l<=20.5):
                    num=570
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=571
                if(l>=1.5 and l<3.5):
                    num=572
                if(l>=3.5 and l<=20.5):
                    num=573
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=574
                if(l>=1.5 and l<3.5):
                    num=575
                if(l>=3.5 and l<=20.5):
                    num=576
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=577
                if(l>=1.5 and l<3.5):
                    num=578
                if(l>=3.5 and l<=20.5):
                    num=579
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=580
                if(l>=1.5 and l<3.5):
                    num=581
                if(l>=3.5 and l<=20.5):
                    num=582
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=583
                if(l>=1.5 and l<3.5):
                    num=584
                if(l>=3.5 and l<=20.5):
                    num=585
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=586
                if(l>=1.5 and l<3.5):
                    num=587
                if(l>=3.5 and l<=20.5):
                    num=588
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=589
                if(l>=1.5 and l<3.5):
                    num=590
                if(l>=3.5 and l<=20.5):
                    num=591
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=592
                if(l>=1.5 and l<3.5):
                    num=593
                if(l>=3.5 and l<=20.5):
                    num=594
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=595
                if(l>=1.5 and l<3.5):
                    num=596
                if(l>=3.5 and l<=20.5):
                    num=597
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=598
                if(l>=1.5 and l<3.5):
                    num=599
                if(l>=3.5 and l<=20.5):
                    num=600
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=601
                if(l>=1.5 and l<3.5):
                    num=602
                if(l>=3.5 and l<=20.5):
                    num=603
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=604
                if(l>=1.5 and l<3.5):
                    num=605
                if(l>=3.5 and l<=20.5):
                    num=606
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=607
            if(l>=1.5 and l<3.5):
                num=608
            if(l>=3.5 and l<=20.5):
                num=609



    if(open>=9.94 and open<=10.6):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            num=610
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=611
            if(l>=1.5 and l<3.5):
                num=612
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=613
            if(l>=1.5 and l<3.5):
                num=614
            if(l>=3.5 and l<20.5):
                num=615
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=616
            if(l>=1.5 and l<3.5):
                num=617
            if(l>=3.5 and l<=20.5):
                num=618
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=619
            if(l>=1.5 and l<3.5):
                num=620
            if(l>=3.5 and l<=20.5):
                num=621
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=622
            if(l>=1.5 and l<3.5):
                num=623
            if(l>=3.5 and l<=20.5):
                num=624
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=625
            if(l>=1.5 and l<3.5):
                num=626
            if(l>=3.5 and l<=20.5):
                num=627
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=628
            if(l>=1.5 and l<3.5):
                num=629
            if(l>=3.5 and l<=20.5):
                num=630
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=631
            if(l>=1.5 and l<3.5):
                num=632
            if(l>=3.5 and l<=20.5):
                num=633
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=634
            if(l>=1.5 and l<3.5):
                num=635
            if(l>=3.5 and l<=20.5):
                num=636
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=637
            if(l>=1.5 and l<3.5):
                num=638
            if(l>=3.5 and l<=20.5):
                num=639
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=640
            if(l>=1.5 and l<3.5):
                num=641
            if(l>=3.5 and l<=20.5):
                num=642
                
    return num














#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
#print('今天是'+d)

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
         '2019-03-31','2019-06-30','2019-09-30','2019-12-31',
         '2020-03-31','2020-06-30','2020-09-30','2020-12-31']
rq_int_list=[20150331,20150630,20150930,20151231,
         20160331,20160630,20160930,20161231,
         20170331,20170630,20170930,20171231,
         20180331,20180630,20180930,20181231,
         20190331,20190630,20190930,20191231,
         20200331,20200630,20200930,20201231]





#获取需要除权的表

dm_list=[]
tjts=256
dm_update_list=[]
dm=''
open=0
high=0
low=0
close=0
qyt_close_list=[]
dt_open_list=[]
dt_high_list=[]
dt_low_list=[]
dt_close_list=[]
open_list=[]
high_list=[]
low_list=[]
close_list=[]
 
 
 
sql = "SELECT dm  FROM kxfzb where tag1='备选'  order by id "
cursor.execute(sql)
for a in cursor.fetchall():
    dm_list.append(a[0])
print(len(dm_list))
     
 
 
for k in range(0,len(dm_list)) :
 
 
    dm='tb'+dm_list[k]
 
    print(dm)
 
    qyt_close_list=[]
    dt_open_list=[]
    dt_high_list=[]
    dt_low_list=[]
    dt_close_list=[]
    date_dt_list=[]
    open_list=[]
    high_list=[]
    low_list=[]
    close_list=[]
 
 
 
    sql = "select t.close from (select id ,close from %s order by id desc limit %d) t order by t.id limit %d"
    data = (dm,tjts+1,tjts)
    cursor.execute(sql % data)
    for a in cursor.fetchall():
        qyt_close_list.append(a[0]) 
  
    sql = "select t.open,t.high,t.low,t.close,t.date from (select id,date,open,high,low,close from %s order by id desc limit %d) t order by t.id "
    data = (dm,tjts)
    cursor.execute(sql % data)
    for a in cursor.fetchall():
        dt_open_list.append(a[0])
        dt_high_list.append(a[1])
        dt_low_list.append(a[2])
        dt_close_list.append(a[3])
        date_dt_list.append(a[4])
  
    for i in range(tjts):
        open_list.append((dt_open_list[i]-qyt_close_list[i])*100/qyt_close_list[i])
        high_list.append((dt_high_list[i]-qyt_close_list[i])*100/qyt_close_list[i])
        low_list.append((dt_low_list[i]-qyt_close_list[i])*100/qyt_close_list[i])
        close_list.append((dt_close_list[i]-qyt_close_list[i])*100/qyt_close_list[i])
  
  
    for i in range(tjts):
        open=open_list[i]
        high=high_list[i]
        low=low_list[i]
        close=close_list[i]
        num=0
        num=bm(open,high,low,close)
  
        if(num==0):
            print(dm,date_dt_list[i],open,high,low,close)
            dm_update_list.append(dm[2:])
 
 
dm_cq_list=[]
dm_cq_list=dm_update_list

#dm_cq_list=['300480', '300522', '300647', '300659', '300682', '600963', '603078']
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




#----------------------------------------------------数据校验


sqll = "SELECT close FROM tb603986 order by id desc limit 1 "
cursor.execute(sqll)
for row in cursor.fetchall():
    yz = row[0]


print(yz)

df1=jq.get_price("603986.XSHG",  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
df1.reset_index(inplace=True,drop=False)
lists=df1.values.tolist()
mbz = lists[len(lists)-1][2]

print(mbz)

if(yz==mbz):
    print("数据校验成功")
    print('**************************恭喜！所有数据为最新******************************') 
    print("job done")
    pass
else:
    print("数据校验失败，请检查")
    print('**************************数据更新失败******************************') 




  

# 关闭连接
cursor.close()
connect.close()