'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
from _datetime import datetime
 
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
    db='xg',
    charset='utf8'
)
cursor = connect.cursor()

#获取现有代码表
dm_old_list=[]
sql = "SELECT dm ,name FROM dmb order by id "
cursor.execute(sql)
for a in cursor.fetchall():
    dm_old_list.append(a)  
    
#获取现有日期表
date_old_list=[]
sql = "SELECT date FROM rqb order by id "
cursor.execute(sql)
for b in cursor.fetchall():
    date_old_list.append(b)

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
date_list=[]
sql = "SELECT date FROM szzs order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    date_list.append(row)
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
    date_old_list.append(c)
    
#对比新老代码表和日期表
date_insert_list=[]
dm_insert_list=[]
dm_delete_list=[]
date_insert_list=date_new_list-date_old_list
dm_insert_list=dm_new_list-dm_old_list
dm_delete_list=dm_old_list-dm_new_list
    
   
#更新代码表
total=0
for m in range(len(dm_insert_list)):
    sql = "INSERT INTO dmb (dm,name) VALUES ( '%s', '%s')"
    data = (dm_insert_list[m][0],dm_insert_list[m][1])
    cursor.execute(sql % data)
    connect.commit()
    total=total+cursor.rowcount
print('成功插入', total, '支股票')
total=0
for n in range(len(dm_delete_list)):
    sql = "delete from dmb where dm='s%'"
    data = (dm_delete_list[n][0])
    cursor.execute(sql % data)
    connect.commit()
    total=total+cursor.rowcount
print('成功删除', total, '支股票')


#更新股票数据表  
#1.删除停止上市的表
total=0
for o in range(len(dm_delete_list)):
    sql = "drop table s% "
    data = ('TB'+dm_delete_list[o][0])
    cursor.execute(sql)
    connect.commit()
    total=total+cursor.rowcount
print('成功删除', total, '张股票表')

#2.插入新上市的表
#更新股票数据 更新日期2019-5-10
for i in range(0, len(df2)):#len(df)
    df1=jq.get_price(df2.iloc[i]['dm'], start_date='2019-05-09',end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')#[total-total-total:]
    df1.reset_index(inplace=True,drop=False)
    list3=df1.values.tolist()
    #插入数据 
    for j in range(len(list3)):
        try:
            sql = "INSERT INTO %s (date,open,close,high,low,volume) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )"
            date = datetime.date(datetime.fromtimestamp(list3[j][0].timestamp()))        
            data = ('TB'+df2.iloc[i]['dm'][:6],date,list3[j][1],list3[j][2],list3[j][3],list3[j][4],list3[j][5])
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()  # 事务回滚
            continue
        else:
            connect.commit()# 事务提交
    print(df2.iloc[i]['dm'][:6]+'数据更新完成')
print('所有数据更新完成')

# 关闭连接
cursor.close()
connect.close()