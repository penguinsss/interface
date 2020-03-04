# 不是很安全，但却很实用，窃取令牌
import requests
# 获取验证码，登录，点击我的订单

resp_verify = requests.get('http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.8333015742274967')
cookies = resp_verify.cookies
print(cookies)

resp_login = requests.post('http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.5339500519807754',
                           data={"username": "18682971383", "password": "123321", "verify_code": "8888"},
                           cookies=cookies)
resp_order = requests.get('http://127.0.0.1/Home/Order/order_list.html', cookies=cookies)

print(resp_verify.content)
print(resp_login.json())
print(resp_order.text)
