'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
 
#jqdata认证
jq.auth('13401179853','king179853')
'''
#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print(d)
#调用jqdata获取数据
df = jq.get_fundamentals(jq.query(
        jq.valuation.code, jq.valuation.market_cap, jq.valuation.pe_ratio, jq.income.total_operating_revenue,jq.income.np_parent_company_owners 
    ), date='2019-5-10')
print(df[1:2])
'''

'''
#最上面的数据是最新的
df2=jq.get_money_flow(['002197.XSHE',], start_date='2019-05-1', end_date='2019-05-10', fields=['net_amount_xl','net_amount_l','net_amount_m','net_amount_s'])
print(df2)
'''

from jqdatasdk import finance
df3=finance.run_query(jq.query(finance.STK_SHAREHOLDER_FLOATING_TOP10.shareholder_name,finance.STK_SHAREHOLDER_FLOATING_TOP10.share_number,finance.STK_SHAREHOLDER_FLOATING_TOP10.share_ratio).filter(finance.STK_SHAREHOLDER_FLOATING_TOP10.code=='600276.XSHG',finance.STK_SHAREHOLDER_FLOATING_TOP10.end_date>='2019-03-31',))
print(df3)


'''
#数据整理
df.drop(columns=['start_date', 'end_date','type','name'],axis=1,inplace=True);
df.rename(columns={'display_name':'name'},inplace=True)
df.reset_index(inplace=True,drop=False)
df.rename(columns={'index':'dm'},inplace=True)
for i in range(0, len(df)):
    df.iloc[i]['dm']=df.iloc[i]['dm'][:6] 
list=df.values.tolist()

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

# 插入数据
total=0;
for i in range(len(list)):
    #TIMESTAMP(8)　| YYYYMMDD
    sql = " create table IF NOT EXISTS %s(id int primary key auto_increment,date varchar(16) unique ,open Float(5,2) default  0.00,close Float(5,2) default  0.00,high Float(5,2) default  0.00,low Float(5,2) default  0.00,volume Float(14,2) default  0.00);"
    data = ('TB'+list[i][0])
    cursor.execute(sql % data)
    connect.commit()
    print(data+'创建成功')
    total=total+1
print('成功创建', total, '张表')

# 关闭连接
cursor.close()
connect.close()
'''