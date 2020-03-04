"""
    响应.status_code 状态码
    响应.url 请求url
    响应.encoding 查看响应头部字符编码
    响应.headers 头信息
    响应.cookies cookie信息
    响应.text 文本形式的响应内容
    响应.content 字节形式的响应内容，图片等
    响应.json() JSON形式的响应内容
"""
import requests

resp = requests.get('http://www.baidu.com')
print(resp.status_code)
print(resp.url)
print(resp.encoding)
print(resp.headers)
print(resp.cookies)
print(resp.text)
print(resp.content)


