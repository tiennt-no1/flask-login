# # Import the 'modules' that are required for execution for Selenium test automation
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# import sys
# from faker import Faker
# fake = Faker()
# sys.path.append("C:/Users/tiennt/Desktop/code lab/flask-login")
# from app import User, app, db

# # Fixture for Chrome
# @pytest.fixture(scope="class")
# def chrome_driver_init(request):
#     chrome_driver = webdriver.Chrome()
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()


# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_URL_Chrome():
#     def test_open_url(self):
#         with app.app_context():
#             self.driver.get('http://localhost:5000')
#             username = fake.profile(fields=['username'])['username']
#             password = fake.password()
#             self.driver.find_element("id", "register_button").click()
#             assert self.driver.find_element("name", "username")
#             assert self.driver.find_element("name", "password")
            
#             while User.query.filter(User.username == username).first():
#                 #sake new username 
#                 username = fake.profile(fields=['username'])['username'] 
#             self.driver.find_element("name", "username").send_keys(username)
#             self.driver.find_element("name", "password").send_keys(password)
#             self.driver.find_element("id", "submit_register").click()

#             user = User.query.filter(User.username == username).first()
#             assert user

#             # self.driver.find_element("id", "login_button").click()
#             # auto navigate to login page after register
#             self.driver.find_element("name", "username").send_keys(username)
#             self.driver.find_element("name", "password").send_keys(password)

#             self.driver.find_element("id", "submit_login_button").click()
#             # should auto navigate to wellcome page
#             assert self.driver.find_element("id", "wellcome_span").text == "WELCOME"
#             assert self.driver.find_element("id", "logout_button")
#             # tear down
#             db.session.delete(user)
#             db.session.commit()
#             sleep(1)





