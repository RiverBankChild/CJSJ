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


date_list=[]
sql1 = "SELECT date FROM rqb order by id "
cursor.execute(sql1)
for it in cursor.fetchall():
    date_list.append(it[0])
    
 
 
end_date = '';
fs = '';
for i in range(0, len(dm_list)):
    for k in range(0,len(date_list)):
        
        fs = '';
        end_date = date_list[k] + " 23:00:00"
        df1=jq.get_price(dm_list[i],  count = 240 ,end_date=end_date, frequency='minute', fields=['close'], skip_paused=True, fq='pre')
        df1.reset_index(inplace=True,drop=False)
        list=df1.values.tolist()
        if(len(list) == 240 and list[0][0].__str__()[11:]=='09:31:00'):
            for j in range(len(list)):
                time = ',' + list[j][0].__str__()[11:] + "-" + str(list[j][1]);
                
                if j == 0:  
                    fs+=time[1:];
                else:
                    fs+=time
            
            sql = "update %s  set fs = '%s' where date = '%s'"
            data = ('TB'+dm_list[i][:6],fs,date_list[k])
            cursor.execute(sql % data)
            connect.commit()  # 事务提交  
        else:
            print('分时数据采集出错')
            break
        print(dm_list[i][:6]+'   '+date_list[k]+'分时数据获取完成')
    print(dm_list[i][:6]+'分时数据获取完成')
        
print('所有历史分时数据获取完成')

# 关闭连接
cursor.close()
connect.close()