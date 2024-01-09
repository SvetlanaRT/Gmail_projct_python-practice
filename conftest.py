import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def setup(request):
    with open('utilities/conf.json') as json_file:
        conf = json.load(json_file)

        options = webdriver.ChromeOptions()

        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        # Remove the --headless option to run in non-headless mode
        # options.add_argument("--headless")

        driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                                  options=options)
        setup.domain = conf['baseUrl']
        url = f'{setup.domain}'

        driver.get(url)
        print(driver.title)
        driver.save_screenshot('./save_screenshot_method.png')
        driver.implicitly_wait(10)
        driver.maximize_window()

        request.cls.driver = driver

        yield
        time.sleep(2)
        driver.quit()
