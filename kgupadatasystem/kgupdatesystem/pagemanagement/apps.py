from django.apps import AppConfig


class PagemanagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagemanagement'

import unittest
from selenium import webdriver

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.luogu.com.cn/auth/login")

    def test_empty_username(self):
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")
        username_field.clear()
        password_field.clear()
        login_button.click()
        error_message = self.driver.find_element_by_id("error-message").text
        self.assertEqual(error_message,"请输入用户名")

    def test_empty_password(self):
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")
        username_field.clear()
        password_field.clear()
        login_button.click()
        error_message = self.driver.find_element_by_id("error-message").text
        self.assertEqual(error_message,"请输入密码")

    def test_invalid_credentials(self):
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")
        username_field.clear()
        username_field.send_keys("wrong_username")
        password_field.clear()
        password_field.send_keys("wrong_password")
        login_button.click()

        error_message = self.driver.find_element_by_id("error-message").text
        self.assertEqual(error_message,"用户名或密码错误")

    def test_valid_credentials(self):
        username_field = self.driver.find_element_by_id("username")
        password_field = self.driver.find_element_by_id("password")
        login_button = self.driver.find_element_by_id("login-button")

        username_field.clear()
        username_field.send_keys("correct_username")
        password_field.clear()
        password_field.send_keys("correct_password")
        login_button.click()
        current_url = self.driver.current_url
        self.assertEqual(current_url,"https://www.luogu.com.cn/")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()