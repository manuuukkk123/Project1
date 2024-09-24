import pytest
# @pytest.fixture()
# def setup():
#     print("I will be executing first")
#     yield
#     print("I will be executing last")

@pytest.fixture()
def dataLoad():
    print("user profile data has been created")
    return ["Rahul","Shetty","rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome", "Manu"),("Firefox","Kumar",),("IE","SS")])
def crossBrowser(request):
    return request.param

