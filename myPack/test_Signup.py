import pytest

@pytest.yield_fixture()
def setUp():
    print("Opening URL to Signup")
    yield
    print("Closing browser after Signup")

def test_signupByemail(setUp):
    print("this is signup by email test")

def test_signupByfacebook(setUp):
    print("this is signup by facebook test")
