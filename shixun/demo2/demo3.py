# -*- codeing = utf-8 -*-
# @time : 2021/11/18 15:41
# @Author : 王博
# @File : demo3.py
# @Software: PyCharm

'''
tup1 = ()  #创建空的元组
print(type(tup1))

#tup2 = (50)    #<class 'int'>
#tup2 = (50,)
tup2 = (50,60,70)

print(type(tup2))
'''

tup1 = ("abc","des",2000,2020,333,444,555)

'''
print(tup1[0])
print(tup1[-1])     #访问最后一个元组
print(tup1[1:5])   #左闭右开 进行切片
'''

'''
#改
tup1 = (12,34,56)

tup1[0] = 100    #不允许修改
'''

'''
#增 连接了
tup1 = (12,34,56)
tup2 = ("abc","xyz")

tup = tup1 +tup2
print(tup)
'''

'''
#删
tup1 = (12,34,56)
print(tup1)
del tup1         #删除了整个元组变量
print("删除后：")
print(tup1)
'''

#字典的定义
info = {"id":1,"name":"张艺兴","age":30}

#字典的访问
'''
print(info["name"])
print(info["age"])

#访问了不存在的键
#print(info["gender"])       #直接访问会报错

#print(info.get("gender"))     #使用get方法·没有找到对应的键，默认返回none
print(info.get("age",18))
print(info.get("gender","m"))    #没有找到的时候，可以设定默认值
'''

'''
#增

newID = input("请输入新的学号")
info["id"] = newID

print(info["id"])
'''


#删  del   clear
# print("删除前：%s"%info["name"])
#
# del info["name"]

#print("删除后：%s"%info["name"])   #删除了指定键值对后，再次访问会报错

'''
print("删除前:%s"%info)

del info
print("删除后:%s"%info)      #删除字典后再访问。报错
'''

'''
print("清空前：%s"%info)

info.clear()

print("清空后：%s"%info)
'''

'''
#改
info["age"] = 20

print(info["age"])
'''

'''
#查 （遍历）
print(info.keys())      #得到所有的键（列表）

print(info.values())      #得到所有的值（列表）

print(info.items())     #得到所有的项（列表），每个键值是一个元组
'''

'''
#遍历所有的键
for key in info.keys():
    print(key)

#遍历所有的值
for value in info.values():
    print(value)
'''

'''
#遍历所有的值
for key,value in info.items():
    print(value)
'''

'''
#遍历所有的键值对
for key,value in info.items():
    print("key=%s,value=%s"%(key,value))
'''

#使用枚举函数，同时拿到列表中的下标和元素内容
mylist = ["a","b","c","d"]
print(enumerate(mylist))
for i,x in enumerate(mylist):
    print(i,x)





