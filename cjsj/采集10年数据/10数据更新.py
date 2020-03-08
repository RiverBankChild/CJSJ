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


#超参
ksrq='2009-11-05'




#认证
jq.auth('13401179853','king179853')

#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print('今天是'+d)

#建立连接 获取游标
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg2',
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
szzs_df=jq.get_price('000001.XSHG',  start_date=ksrq,end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
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
    insert_df=jq.get_price(dm_insert_sh_list[q],  start_date=ksrq,end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
    insert_df.reset_index(inplace=True,drop=False)
    insert_list=insert_df.values.tolist()
    for s in range(len(insert_list)):
        sql = "INSERT INTO %s (date,open,close,high,low,cjl) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )" 
        date = datetime.date(datetime.fromtimestamp(insert_list[s][0].timestamp()))       
        data = ('TB'+dm_insert_list[q][0],date,insert_list[s][1],insert_list[s][2],insert_list[s][3],insert_list[s][4],insert_list[s][5])
        cursor.execute(sql % data)
        connect.commit()
    print('TB'+dm_insert_sh_list[q][:6],'收盘价数据获取完成')
    
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
            
    print('TB'+dm_sh_list[q][:6],'数据更新完成')  
print('所有表所有数据更新完毕....................................') 


print('**************************恭喜！所有数据为最新******************************')    
  

# 关闭连接
cursor.close()
connect.close()