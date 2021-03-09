'''
Methods in unittest framework:
1. setup: Executes before every test method call
2. teardown: Executes after every test method call
3. setUpClass: Executes only once test method call
4. tearDownClass: Executes only once after test method execution
5. setUpModule: Outside class. First execution
6. tearDownModule: Outside class. Last execution
'''
import unittest

def setUpModule():
    print("setUpModule")

def tearDownModule():
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("This is logout test")

    @classmethod
    def setUpClass(cls):
        print("Open Application")

    @classmethod
    def tearDownClass(cls):
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is postpaid Recharge test")

if __name__ == "__main__":
    unittest.main()
