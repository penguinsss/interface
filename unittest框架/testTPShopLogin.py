import requests
import unittest

from parameterized import parameterized

from unittest框架.utils import build_data


class TestTPShopLogin(unittest.TestCase):
    session = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()

    @parameterized.expand(build_data())  # 最外层是列表，元素可以是列表也可以是元组
    def test_login(self, username, password, verify_code, expect, status):
        resp = self.session.get('http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.8333015742274967')
        self.assertEqual("image/png", resp.headers.get("Content-Type"))

        resp = self.session.post('http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.5339500519807754',
                                 data={"username": username, "password": password, "verify_code": verify_code}
                                 )
        jsonData = resp.json()
        print('登录接口的json数据：', jsonData)

        self.assertEqual(200, resp.status_code)
        status_arg = jsonData.get('status')
        self.assertEqual(status, status_arg)
        self.assertIn(expect, jsonData.get('msg'))
        if status_arg == 1:
            self.assertEqual('东皇太一', jsonData.get('result').get('nickname'))
