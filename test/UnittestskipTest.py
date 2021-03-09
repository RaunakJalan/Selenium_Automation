'''
Methods to skip tests in unittest framework: Used to skip tests
1. Skip Test
2. Skip Test with Reason
3. Skip Test with Based on condition
'''

import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):  #skipped
        print("This is search test")

    @unittest.skip("I am skipping this test method because it is not ready")
    def test_advancedsearch(self):
        print("This is Advanced search test")

    @unittest.skipIf(1==1, "Numbers are not equal")
    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid Recharge test")

    def test_loginbygmail(self):
        print("This is login by Gmail")

    def test_loginbytwitter(self):
        print("This is login by twitter")


if __name__ == "__main__":
    unittest.main()
