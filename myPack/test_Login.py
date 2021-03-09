import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to Login")
    yield
    print("Closing browser after Login")

def test_loginByemail(setUp):
    print("this is Login by email test")

def test_loginByfacebook(setUp):
    print("this is Login by facebook test")
