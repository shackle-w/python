# -*- codeing = utf-8 -*-
# @time : 2021/11/20 13:32
# @Author : 王博
# @File : testSqlite.py
# @Software: PyCharm


import sqlite3

# conn = sqlite3.connect("test.db")   #打开或创建数据库文件
#
# print("Opened database successfully")



conn = sqlite3.connect("test.db")   #打开或创建数据库文件

print("成功打开数据库")

sql ='''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);
'''
c = conn.cursor()   #获取游标
conn.commit()       #提交数据库操作
conn.close()        #关闭数据路连接

print("成功建表")



#3.插入数据
conn = sqlite3.connect("test.db")   #打开或创建数据库文件

print("成功打开数据库")

sql1 =''' 
  insert into company（id,name,age,address,salary)
  values(1,'张三',32,'郑州',8000
'''

sql1 ='''  
  insert into company（id,name,age,address,salary)
   values(2,'李四',30,'洛阳',15000
'''
c = conn.cursor()   #获取游标
conn.commit()       #提交数据库操作
conn.close()        #关闭数据路连接

print("插入数据完毕")


#4.查询数据
conn = sqlite3.connect("test.db")   #打开或创建数据库文件

print("成功打开数据库")

c = conn.cursor()     #获取游标

sql = "select id,name,address,salary from company"

cursor = c.execute(sql)  #执行sql语句

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3],"\n")

conn.close()        #关闭数据路连接

print("查询完毕")




