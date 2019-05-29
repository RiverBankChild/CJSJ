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
print(d)


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

df1=jq.get_price('000001.XSHG',  end_date='2019-05-10', frequency='daily', fields=['open', 'close', 'high', 'low', 'volume'], skip_paused=True, fq='pre')
df1.reset_index(inplace=True,drop=False)
list=df1.values.tolist()
#插入数据 

zjl_df=jq.get_money_flow(['000001.XSHG'], start_date='2015-01-01', end_date='2019-05-22', fields=['date','change_pct'])
print(zjl_df)
zjl_list=zjl_df.values.tolist()

#total=0;
#for p in range(0,len(zjl_list)):
 #   sql = "update %s set zdf=%.2f, cdd=%.2f ,  dd=%.2f  ,  zd=%.2f  ,  xd=%.2f  where date='%s'"
 #   data=('TB'+dmb_list[o][:6],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],zjl_list[p][5],datetime.date(datetime.fromtimestamp(zjl_list[p][0].timestamp())))
 #   cursor.execute(sql % data)
  #  connect.commit()  # 事务提交
#    total=total+cursor.rowcount
#print(dmb_list[o],'数据插入完毕,','共更新了',total,'条数据')


# 关闭连接
cursor.close()
connect.close()