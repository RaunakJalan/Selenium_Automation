'''
@pytest.fixture(): Executes specific method before every test method
@pytest.yield_fixture(): Executes specific method before and after every test method
'''
import pytest

@pytest.fixture

def setup():
    print("Once before every method")

def testmethod1(setup):
    print("This is test method 1")

def testmethod2(setup):
    print("This is test method 2")
