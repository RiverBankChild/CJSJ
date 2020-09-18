#数据修正

import pymysql


connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='xg',
    charset='utf8'
)
cursor = connect.cursor()

dm_list=[]

sql = "SELECT dm  FROM dmb  "
cursor.execute(sql)
for a in cursor.fetchall():
    dm_list.append(a[0])
print(len(dm_list))


for s in range(0,len(dm_list)):
    
    sql = " delete from %s where date='%s'" 
    try:     
        data = ('TB'+dm_list[s],'2020-08-27')
        cursor.execute(sql % data) 
    except Exception as e:
        connect.rollback()  # 事务回滚
        continue
    else:
        connect.commit()  # 事务提交
        
    print(dm_list[s])



# 关闭连接
cursor.close()
connect.close()