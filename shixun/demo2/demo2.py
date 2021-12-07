# -*- codeing = utf-8 -*-
# @time : 2021/11/18 11:19
# @Author : 王博
# @File : demo2.py
# @Software: PyCharm


#namelist = [] #定义一个空的列表

namelist = ["小张","小王","小李"]
'''
textlist = [1,"测试"]        #列表中可以存储混合类型
print(type(textlist[0]))
print(type(textlist[1]))

print(namelist[0])
print(namelist[1])
print(namelist[2])
'''

'''
for name in namelist:
    print(name)


#print(len(namelist))        #len()可以得到列表的长度

length = len(namelist)

i = 0

while i < length:
    print(namelist[i])
    i += 1
'''


#增加:[append]
'''
print("--------增加前·名单列表的数据--------")
for name in namelist:
    print(name)

nametemp = input("请输入添加学生的姓名：")
namelist.append(nametemp)         #在末尾追加一个元素

print("--------增加后·名单列表的数据--------")
for name in namelist:
    print(name)
'''

'''
a = [1,2]
b = [3,4]
a.append(b)    #将列表当作一个元素·加入到列表中
print(a)

a.extend(b)   #将b列表中每个元素·逐一追加到a列表中
print(a)
'''

'''
#增：  [insert]

a = [0,1,2]
a.insert(1,3)   #第一个变量表示下标，第二个表示元素（对象）
print(a)
'''

'''
#删   [del]  [pop]    [remove]

movieName = ["加勒比海盗","黑客帝国","第一滴血","指环王","速度与激情","指环王"]

print("--------增加前·电影列表的数据--------")
for name in movieName:
    print(name)

#del movieName[2]     #在指定位置删除一个元素
#movieName.pop()      #弹出末尾最后一个元素
movieName.remove("指环王") #直接删除指定内容的元素

print("--------增加后·电影列表的数据--------")
for name in movieName:
    print(name)
'''

'''
#改

print("--------修改前·名单列表的数据--------")
for name in namelist:
    print(name)

namelist[1] = "小红"

print("--------修改后·名单列表的数据--------")
for name in namelist:
    print(name)
'''

'''
#查  [in] [not in]

findName = input("请输入你要查找学生姓名：")

if findName in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")
'''


mylist = ["a","b","c","a","b"]

'''
print(mylist.index("a",1,4))  #可以查找指定下标范围的元素，并返回对应数据的小标

print(mylist.index("a",1,3)    #范围区间，左闭右开[1，3）  ，找不到会报错
'''

'''
print(mylist.count("c"))     #统计某个元素出现几次
'''

'''
#排序和反转
a = [1,4,2,3]
print(a)
a.reverse()  #将列表所有元素反转
print(a)

a.sort()      #升序
print(a)
a.sort(reverse=True)  #降序
print(a)
'''


schoolName = [[],[],[]]  #有3个元素的空列表，每个元素都是一个空列表

schoolName = [["北京大学","清华大学"],["南开大学","天津大学","南京师范"],["山东大学","中国海事"]]

print(schoolName[0][0])

import random

offices = [[],[],[]]

names = ["A","B","C","D","E","F","G","H"]

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d的人数为：%d"%(i,len(office)))
    i = i + 1
    for name in office:
        print("%s"%name,end = "\t")
    print("\n")
    print("-"*20)

