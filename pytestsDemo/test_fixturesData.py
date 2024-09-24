from pytestsDemo.BaseClass import BaseClass


import pytest
@pytest.mark.usefixtures("dataLoad")


class TestExample2(BaseClass):

    def test_editprofile(self,dataLoad):
        log=self.getlogger()
        log.info(dataLoad[0])
        log.info(dataLoad[2])

        print(dataLoad[2])