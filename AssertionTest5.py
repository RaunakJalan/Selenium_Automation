#assertGreater, assertGreaterEqual, assertLess and assertLessEqual
import unittest


class Test(unittest.TestCase):
    def testName(self):

        #assertGreater
        #self.assertGreater(100,10,"100 is less or equal than number")#passed
        #self.assertGreater(100,100,"100 is less or equal than number")#failed
        #self.assertGreater(100,104,"100 is less or equal than number")#failed

        #assertGreaterEqual
        #self.assertGreaterEqual(100,10,"100 is less than number")#passed
        #self.assertGreaterEqual(100,100,"100 is less than number")#passed
        #self.assertGreaterEqual(100,104,"100 is less than number")#failed

        #assertLess
        #self.assertLess(100,10,"100 is greater or equal than number")#failed
        #self.assertLess(100,100,"100 is greater or equal than number")#failed
        #self.assertLess(100,104,"100 is greater or equal than number")#passed

        #assertLessEqual
        #self.assertLessEqual(100,10,"100 is greater than number")#failed
        #self.assertLessEqual(100,100,"100 is greater than number")#passed
        self.assertLessEqual(100,104,"100 is greater than number")#passed



if __name__ == "__main__":
    unittest.main()
