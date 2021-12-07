# -*- codeing = utf-8 -*-
# @time : 2021/11/18 23:06
# @Author : 王博
# @File : demo3.py
# @Software: PyCharm

'''
#发生异常
print("----------test------1--------")

f = open("123.txt")       #用只读模式打开了一个不存在的文件，报错

print("----------test------2--------")    #这句代码不会执行
'''

'''
#捕获异常
try:
    print("----------test------1--------")

    f = open("123.txt")

    print("----------test------2--------")
except IOError:   #文件没找到·属于IO异常（输入输出异常）
    pass       #捕获异常后，执行的代码
'''

'''
try:
    print(num)
#except IOError:         #异常类型想要被捕获，需要一致
except NameError:
    print("产生错误了")
'''

'''
try:
    print("----------test------1--------")
    f = open("123.txt")
    print("----------test------2--------")

    print(num)
except(NameError,IOError):   #将可能产生的所有异常类型，都放到下面的小括号中
    print("产生错误了")
'''

'''
#获取错误描述
try:
    print("----------test------1--------")
    f = open("123.txt")
    print("----------test------2--------")

    print(num)
except(NameError,IOError)as result:   #将可能产生的所有异常类型，都放到下面的小括号中
    print("产生错误了")
    print(result)
'''

'''
#捕获所有的异常
try:
    print("----------test------1--------")
    f = open("text.txt")
    print("----------test------2--------")

    print(num)
except Exception as result:   #Exception可以承接任何异常
    print(result)
'''

import time
#try....finally 和嵌套

try:
    f = open("test1.txt","r")

    try:
        while True:
            content = f.realine()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常。。。。")








