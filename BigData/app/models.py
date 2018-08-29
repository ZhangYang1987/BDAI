import sqlite3
import pandas as pd
#连接数据库，创建表
# conn=sqlite3.connect('upload_info')
# print("Opened database successfully")
# cursor=conn.cursor()
# sql_string='create table upload_info' \
#            '(ID Text primary key not null,' \
#            'file_name text not null,' \
#            'file_size text not null,' \
#            'file_type text not null)'
# cursor.execute(sql_string)
# cursor.close()
# print("Table created successfully")
# conn.commit()
# conn.close()

#查询
conn=sqlite3.connect('upload_info')
c=conn.cursor()
# c.execute('select * from upload_info')
c.execute('select * from upload_info where file_type="xlsx"')
# c.execute('PRAGMA TABLE_INFO (upload_info)')
result=c.fetchall()
results=pd.DataFrame(result)
results.columns=['ID','file_name','file_size','file_type']
for i in range(len(results)):
    print(results.loc[i])
# print(results)
conn.close()

#插入数据
# conn=sqlite3.connect('upload_info')
# c=conn.cursor()
# c.execute('insert into upload_info(ID,file_name,file_size,file_type) values("1","test","4MB","mysql")')
# c.close()
# print('Insert data successfully')
# conn.commit()
# conn.close()

#删除数据
# conn=sqlite3.connect('upload_info')
# c=conn.cursor()
# c.execute('delete from upload_info where file_name="test2"')
# c.close()
# print('Delete data successfully')
# conn.commit()
# conn.close()


#向表中添加字段
# conn=sqlite3.connect('upload_info')
# c=conn.cursor()
# c.execute('alter table upload_info add file_size Text')
# c.close()
# conn.commit()
# conn.close()

#删除表
# conn=sqlite3.connect('upload_info')
# c=conn.cursor()
# c.execute('drop TABLE upload_info')
# c.close()
# conn.commit()
# conn.close()