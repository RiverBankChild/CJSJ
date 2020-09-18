'''
Created on 2019年5月1日
# -*- coding:utf-8 -*-
#要考虑昨天收盘价
@author: Administrator
'''
import pymysql
import jqdatasdk as jq
import time
 
 
#jqdata认证
jq.auth('13401179853','king179853')
#jq.auth('18818807170','123123Zjy')

#定义当前日期
d=time.strftime('%Y-%m-%d',time.localtime(time.time())) 
print(d)

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

#获取现有dm数据
dm_list=[]
sql3 = "SELECT dm FROM dmb order by id "
cursor.execute(sql3)
for row in cursor.fetchall():
    if row[0].startswith('6'):
        r=row[0]+'.XSHG'
    else:
        r=row[0]+'.XSHE'        
    dm_list.append(r)  


    
 
 
end_date = '';
fs = '';
dm = '';
time = '';
date_list=[]
sql3 = ''
for i in range(0, len(dm_list)):
    dm = dm_list[i] 
    date_list=[]
    sql3 = "SELECT date FROM %s order by id "
    data = ('TB'+dm[:6])
    cursor.execute(sql3 % data)
    for it in cursor.fetchall():
        date_list.append(it[0])  
          
    for k in range(0,len(date_list)):
        fs = '';
        end_date = date_list[k] + " 23:00:00"
        df1=jq.get_price(dm,  count = 240 ,end_date=end_date, frequency='minute', fields=['close'], skip_paused=True, fq='pre')
        df1.reset_index(inplace=True,drop=False)
        list=df1.values.tolist()
        if(list[0][0].__str__()[11:]=='09:31:00' and len(list) == 240 ):
            for j in range(len(list)):
                time = ',' + list[j][0].__str__()[11:] + "-" + str(list[j][1]);
                
                if j == 0:  
                    fs+=time[1:];
                else:
                    fs+=time
            
            sql = "update %s  set fs = '%s' where date = '%s'"
            data = ('TB'+dm[:6],fs,date_list[k])
            cursor.execute(sql % data)
            connect.commit()  # 事务提交  
        else:
            pass
        
    print('TB'+dm[:6],'分时数据获取完成')
        
print('所有历史分时数据获取完成')

 
# 关闭连接
cursor.close()
connect.close()