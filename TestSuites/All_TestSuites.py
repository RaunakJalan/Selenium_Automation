import unittest

import sys
sys.path.append("..")

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

#Get all test methods from test classes imported above
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#Sanity test: Login test
# Functional test: Payment test
#Master test: All methods

#Creating test suite
sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
