import requests

url = 'http://www.weather.com.cn/data/sk/101020100.html'
resp = requests.get(url)

# 返回结果数据正常显示，浏览器解析乱码，是因为服务器没有设置返回数据的编码格式，而浏览器默认解码ISO-8859-1
print(resp.json())
print('❀。。。。。。。。。。。')

# ★ 解决办法1
print(resp.content.decode(encoding='utf-8'))
print('❀。。。。。。。。。。。')

# ★ 解决办法2
resp.encoding = 'utf-8'
print(resp.json())
