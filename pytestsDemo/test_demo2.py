# import pytest
#
#
# @pytest.mark.smoke
def test_firstprogram():
    msg== "Hello"
    assert msg == "Hi" , "Test failed because strings donot match"

def test_Secondprogram():
    a=4
    b=6
    assert a+2 == 6, "Additon donot match"