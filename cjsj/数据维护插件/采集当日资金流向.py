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


#获取每日大单量,最上面的数据是最新的
dmb_list=[]
sql = "SELECT dm FROM dmb order by id "
cursor.execute(sql)
for row in cursor.fetchall():
    dmb_list.append(row)
for i in range(0,len(dmb_list)):    
    if dmb_list[i][0].startwith('6'):
        dmb_list[i][0]=dmb_list[i][0]+'.XSHG'
    else:
        dmb_list[i][0]=dmb_list[i][0]+'.XSHE'
for o in range(0,len(dmb_list)):
    zjl_df=jq.get_money_flow([dmb_list[o][0]], start_date='2015-01-01', end_date='2019-05-15', fields=['date','net_amount_xl','net_amount_l','net_amount_m','net_amount_s'])
    print(zjl_df)
    zjl_list=zjl_df.values.tolist()
    total=0;
    for p in range(0,len(zjl_list)):
        try:
            sql = "update %s set  cdd=%.2f ,  dd=%.2f  ,  zd=%.2f  ,  xd=%.2f  where date='%s'"
            data_zjl=('TB'+dmb_list[o][0],zjl_list[p][1],zjl_list[p][2],zjl_list[p][3],zjl_list[p][4],zjl_list[p][0])
            cursor.execute(sql % data_zjl)
        except Exception as e:
            connect.rollback()  # 事务回滚
        else:
            connect.commit()  # 事务提交
            total=total+cursor.rowcount
    print(dmb_list[o][0],'数据插入完毕','共更新了',total,'条数据')
print("所有数据插入完成")


# 关闭连接
cursor.close()
connect.close()