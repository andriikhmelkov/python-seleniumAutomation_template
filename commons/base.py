from selenium import webdriver

import os
import yaml


class Driver(object):

    with open(os.path.dirname(__file__) + "/../configs.yaml", "r") as ymlfile:
        config = yaml.load(ymlfile)

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.email = self.config['email']
        self.password = self.config['password']
        self.app_url = "https://example.com"
        self.browser.implicitly_wait(30)
        self.browser.maximize_window()
        self.reset()

    def reset(self):
        self.browser.get(self.app_url)
        self.browser.delete_all_cookies()

    def teardown(self):
        self.browser.quit()

    def sign_in(self):
        self.browser.find_element_by_id("login-email").send_keys(self.email)
        self.browser.find_element_by_id("login-password").send_keys(self.password)
        self.browser.find_element_by_id("btn-submit").click()
        self.browser.find_elements_by_xpath("//*[contains(text(), 'Welcome')]")
