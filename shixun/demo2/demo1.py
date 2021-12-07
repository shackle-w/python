# -*- codeing = utf-8 -*-
# @time : 2021/11/18 10:09
# @Author : 王博
# @File : demo1.py
# @Software: PyCharm

'''
word = '字符串'
sentence = "这是一个句子"
paragraph ="""
            这是一个段落
            可以由多行组成
"""

print(word)
print(sentence)
print(paragraph)
'''

'''
#my_str = "I'm a student"
my_str = 'I\'m a student'
print(my_str)
'''

'''
#my_str = "Janson said \"I like you \""
my_str = 'Janson said "I like you" '
print(my_str)
'''


str = "zhengzhou"

print(str) # 输出字符串
print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
print(str[0]) # 输出字符串第一个字符
print(str[2:5]) # 输出从第三个开始到第五个的字符
print(str[2:]) # 输出从第三个开始后的所有字符
print(str * 2) # 输出字符串两次
print(str + '你好') # 连接字符串
print(str[:5]) # 输出第五个字母前的所有字符
print(str[0:7:2]) # [起始：终止：步长]


print('------------------------------')
print('hello\nzhengzhou') # 使用反斜杠(\)+n转义特殊字符
print(r'hello\npython') # 在字符串前面添加一个 r，表示原始字符串，不会发生转义




