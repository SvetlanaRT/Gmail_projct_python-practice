import conftest
from util import *

class TestSanity(BaseClass):

    def test_login(self):
        driver=self.driver
        current_url = driver.current_url
        print(current_url)
        assert current_url == f'{conftest.setup.domain}'