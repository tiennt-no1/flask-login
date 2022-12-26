# Import the 'modules' that are required for execution for Selenium test automation
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
 
#Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()
 
@pytest.mark.usefixtures("chrome_driver_init")
class Test_URL_Chrome():
    def test_open_url(self):
        self.driver.get('http://localhost:5000')
        self.driver.maximize_window()
        # import pdb; pdb.set_trace()
        self.driver.find_element("id", "register_button").click()
        assert self.driver.find_element("name", "password").send_keys()
        assert self.driver.find_element("name", "username").send_keys()
        sleep(100)
 
       