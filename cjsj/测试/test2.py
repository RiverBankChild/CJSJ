'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
#认证
jq.auth('13401179853','king179853')


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
df_volandincome = jq.get_fundamentals(jq.query(
        jq.valuation.code, 
        jq.valuation.circulating_market_cap, 
        jq.valuation.pe_ratio, 
        jq.income.total_operating_revenue,
        jq.income.np_parent_company_owners 
        ).filter(
        jq.valuation.code == '603999.XSHG'
        ), date='2019-01-05')
volandincome_list=df_volandincome.values.tolist()
print(volandincome_list)




cursor.close()
connect.close()