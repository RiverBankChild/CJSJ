'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
from _datetime import datetime
 
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


#获取每日大单量,最上面的数据是最新的
dmb_list=[]
sql = "SELECT dm FROM dmb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    if row[0].startswith('6'):
        r=row[0]+'.XSHG'
    else:
        r=row[0]+'.XSHE'        
    dmb_list.append(r)       

for o in range(0,len(dmb_list)):
    zjl_df=jq.get_money_flow([dmb_list[o]], start_date='2015-01-01', end_date='2019-05-15', fields=['date','net_amount_xl','net_amount_l','net_amount_m','net_amount_s'])
    zjl_list=zjl_df.values.tolist()

    total=0;
    for p in range(0,len(zjl_list)):
        try:
            sql = "update %s set  cdd=%.2f ,  dd=%.2f  ,  zd=%.2f  ,  xd=%.2f  where date='%s'"
            #sql = "update %s set dm='%s'  , ltsz=%.2f ,  syl=%.2f  ,  ys=%.2f  ,  jlr=%.2f  where date='%s'"
            data=('TB'+dmb_list[o][:6],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],datetime.date(datetime.fromtimestamp(zjl_list[p][0].timestamp())))
            cursor.execute(sql % data)
        except Exception as e:
            print(e)
            connect.rollback()  # 事务回滚
        else:
            connect.commit()  # 事务提交
            total=total+cursor.rowcount
    print(dmb_list[o],'数据插入完毕,','共更新了',total,'条数据')
print("所有数据插入完成")


# 关闭连接
cursor.close()
connect.close()