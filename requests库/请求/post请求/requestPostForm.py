import requests

# 获取验证码
resp_get_verify_code = requests.get('http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.7023819204519448')
print(resp_get_verify_code.cookies)
# 登录
resp = requests.post('http://localhost/index.php?m=Home&c=User&a=do_login',
                     data={"username": "18682971383", "password": "123321", "verify_code": "8888"})
print('tpshop登录接口返回数据：', resp.json())
