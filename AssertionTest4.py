#assertIn & assertNotIn
import unittest


class Test(unittest.TestCase):
    def testName(self):
        list_test = ["python","selenium","java"]

        #assertIn
        #self.assertIn("python", list_test,"Not present in list")
        #self.assertIn("ruby", list_test,"Not present in list")
        #assertNotIn
        #self.assertNotIn("python", list_test,"Present in list")
        self.assertNotIn("ruby", list_test,"Present in list")

if __name__ == "__main__":
    unittest.main()
