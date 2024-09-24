import pytest

@pytest.mark.usefixtures("setup")


class TestExample:

    def test_fixtureDemo(self):
        print("I will be executing the steps")


    def test_fixtureDemo1(self):
        print("I will be executing the steps in fixtureDemo1")

    def test_fixtureDemo2(self):
        print("I will be executing the steps in fixtureDemo2")

    def test_fixtureDemo3(self):
        print("I will be executing the steps in fixtureDemo3")