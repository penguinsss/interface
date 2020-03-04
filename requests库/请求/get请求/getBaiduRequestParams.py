"""
Requests库是用Python编写的，基于urllib开发的工具，能够进行HTTP协议的接口测试和调试工作，使用简单，功能强大，完全满足HTTP测试需求；
"""
import requests

# 3种方式访问百度搜索，params的值为一个字符串或字典
resp = requests.get('http://www.baidu.com/S?wd=嗯哼')
resp1 = requests.get('http://www.baidu.com/S', params="wd=杨幂")
resp2 = requests.get('http://www.baidu.com/S', params={"wd": "秋刀鱼"})

print(resp.text)
