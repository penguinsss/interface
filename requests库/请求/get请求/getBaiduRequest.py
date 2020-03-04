import requests

resp = requests.get('http://www.baidu.com')
# 解决中文乱码问题，decode解码
print(resp.content.decode(encoding='utf-8'))
