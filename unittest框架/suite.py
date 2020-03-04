import time
import unittest

from unittest框架.HTMLTestRunner import HTMLTestRunner
from unittest框架.testTPShopLogin import TestTPShopLogin
from unittest框架.utils import BASE_DIR

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTPShopLogin))

# unittest.TextTestRunner().run(suite)
file_name = BASE_DIR + '/%s.html' % time.strftime('%Y%m%d_%H%M%S')
with open(file_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f)
    print(runner)
    runner.run(suite)
