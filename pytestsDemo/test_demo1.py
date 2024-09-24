#any pytest should start with test_ or end with _test
#pytest method names should start with test
#any code should be wrapped in one method as shown in given example below
import pytest


@pytest.mark.smoke
def test_firstprogram():
    print("hello")

@pytest.mark.xfail
def test_Greet():
    print("Good Morning")

@pytest.mark.skip
def test_Greetmsg():
    print("Hi Manu")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])