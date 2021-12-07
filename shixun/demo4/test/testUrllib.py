# -*- codeing = utf-8 -*-
# @time : 2021/11/19 14:18
# @Author : 王博
# @File : testUrllib.py
# @Software: PyCharm


import urllib.request

'''
#获取一个get请求
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))     #对获取到的网页源码进行utf-8的解码
'''

'''
#获取一个post请求     模拟用户名密码登录
import urllib.parse
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data = data)
print(response.read().decode('utf-8'))
'''

'''
#超时处理
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("time.out")
'''

'''
response = urllib.request.urlopen("http://www.baidu.com")
#print(response.status)
print(response.getheaders())
print(response.getheader("Server"))
'''



'''
#url = "http://www.douban.com"
url = "http://httpbin.org/post"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding = "utf-8")
req = urllib.request.Request(url = url,data = data,headers = headers,method = "POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

url = "http://www.douban.com"
headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}
req = urllib.request.Request(url = url,headers = headers,)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))











