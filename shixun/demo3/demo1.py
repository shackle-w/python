# -*- codeing = utf-8 -*-
# @time : 2021/11/18 22:19
# @Author : 王博
# @File : demo1.py
# @Software: PyCharm

'''
#函数的定义
def printinfo():
    print("----------------------")
    print("  人生苦短，我用python  ")
    print("----------------------")


#函数的调用
printinfo()
'''

'''
#带参数的函数

def add2Num(a,b):
    c = a + b
    print(c)

add2Num(11,22)
'''

'''
#带返回值的函数

def add2Num(a,b):
    return a + b       #通过return 来返回运算结果

result = add2Num(11,22)
print(result)
'''

'''
#返回多个值的函数

def divid(a,b):
    shang = a / b
    yushu = a % b
    return shang,yushu  #用逗号分隔

sh,yu = divid(5,2)    #需要使用多个值来保存返回内容

print("商：%d，余数：%d"%(sh,yu))
'''

'''
#全局变量和局部变量

def test1():
    a = 300 #局部变量
    print("test1----------修改前：a = %d"%a)
    a = 100
    print("test1----------修改后：a = %d" % a)

def test2():
    a = 500   #不同函数可以定义相同的名字，彼此无关
    print("test2----------a = %d" % a)


test1()
test2()
'''

'''
a = 100  #全局变量

def test1():
    print(a)

def test2():
    print(a)     #调用全局变量a

test1()
test2()
'''

'''
#全局变量和局部变量相同名字

a = 100
def test1():
    a = 300 #局部变量优先使用
    print("test1----------修改前：a = %d"%a)
    a = 100
    print("test1----------修改后：a = %d" % a)

def test2():
    print("test2----------a = %d" % a)  #没有局部变量·默认使用全局变量


test1()
test2()
'''


#在函数中修改全局变量

a = 100
def test1():
    global a  #声明全局变量在函数中的标识符
    print("test1----------修改前：a = %d"%a)
    a = 200
    print("test1----------修改后：a = %d" % a)

def test2():
    print("test2----------a = %d" % a)  #没有局部变量·默认使用全局变量


test1()
test2()

