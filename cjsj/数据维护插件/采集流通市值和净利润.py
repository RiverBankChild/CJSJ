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

#获取流通市值和净利润
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



# 关闭连接
cursor.close()
connect.close()