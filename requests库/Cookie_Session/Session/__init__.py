"""
session对象代表一次用户会话：
    从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开会话能让我们在跨请求时候保持某些参数
    比如在同一个 session 实例发出的所有请求之间保持cookie
"""
import requests

session = requests.Session()
resp_verify = session.get('http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.8333015742274967')
resp_login = session.post('http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.5339500519807754',
                          data={"username": "18682971383", "password": "123321", "verify_code": "8888"}
                          )
resp_order = session.get('http://127.0.0.1/Home/Order/order_list.html')

print(resp_verify.content)
print(resp_login.json())
print(resp_order.text)
