import requests

headers = {"Content-Type":"application/json"}
resp = requests.post('http://182.92.81.159/api/sys/login',  json={
                            "mobile": "13800000002",
                            "password": "123456"
                            }, headers=headers
                     )
print(resp.json())
