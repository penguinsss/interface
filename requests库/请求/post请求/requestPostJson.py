import requests

resp = requests.post('http://182.92.81.159/api/sys/login',
                     json={
                            "mobile": "13800000002",
                            "password": "123456"
                            }
                     )
print('IHRM登录接口返回数据：', resp.json())
