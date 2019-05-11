'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
from _datetime import datetime
 
#jqdata认证
jq.auth('13401179853','king179853')

#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print('今天是'+d)


#建立连接
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg',
    charset='utf8'
)


# 获取游标
cursor = connect.cursor()


#更新上证指数 
df=jq.get_price('000001.XSHG',  end_date=d, frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
df.reset_index(inplace=True,drop=False)
list=df.values.tolist()
total=0;
for j in range(len(list)):
    try:
        sql = "INSERT INTO szzs (date,open,close,high,low,volume) VALUES ( '%s', %.2f ,%.2f ,%.2f ,%.2f,%.2f  )"
        date = datetime.date(datetime.fromtimestamp(list[j][0].timestamp()))        
        data = (date,list[j][1],list[j][2],list[j][3],list[j][4],list[j][5])
        cursor.execute(sql % data)
    except Exception as e:
        connect.rollback()  # 事务回滚
        continue
    else:
        connect.commit()  # 事务提交
        total=total+cursor.rowcount
print('上证指数历史数据更新完成，共更新了',total,'条数据')


#更新日期表
list5=[]
sql = "SELECT date FROM szzs order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    list5.append(row)
for k in range(0,len(list5)):
    try:
        sql = "INSERT INTO rqb (date) VALUES ( '%s')"
        datek =list5[k]         
        datak = (datek)
        cursor.execute(sql % datak)
    except Exception as e:
        connect.rollback()  # 事务回滚
        continue
    else:
        connect.commit()  # 事务提交
        total=total+cursor.rowcount
print('日期表更新完成，共更新了',total,'条数据')
         
#查询代码表
df2=jq.get_all_securities(date=d );
df2.reset_index(inplace=True,drop=False)
df2.rename(columns={'index':'dm'},inplace=True)

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