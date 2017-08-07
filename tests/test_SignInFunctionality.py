import unittest

from commons.base import Driver


class SingInTests(unittest.TestCase):

    @classmethod
    # Executed once per suite at the start
    def setUpClass(cls):
        cls.driver = Driver()
        cls.browser = cls.driver.browser

    # Executed before every test
    def setUp(self):
        self.driver.reset()
        assert "Example Domain" in self.browser.title,\
            "SingIn page is not displayed or couldn't connect"
        assert self.browser.find_element_by_xpath("//* [contains(text(), 'Example Domain')]"),\
            "Example page is not displayed or couldn't connect"

    # Executed once per suite after execution of test cases
    @classmethod
    def tearDownClass(cls):
        cls.driver.teardown()

    # Test cases
    def test_valid_credentials_login(self):
        self.browser.find_element_by_id("login-email").send_keys(self.driver.email)
        self.browser.find_element_by_id("login-password").send_keys(self.driver.password)
        self.browser.find_element_by_id("btn-submit").click()
        assert (self.browser.find_elements_by_xpath("//*[contains(text(), 'Hello, Test user')]")
                and self.browser.find_elements_by_xpath("//*[contains(text(), 'Example Domain')]")),\
            "Welcome page is not displayed or weren't rendered fully"

    def test_invalid_credentials_login(self):
        self.browser.find_element_by_id("login-email").send_keys('invalid@invalid.com')
        self.browser.find_element_by_id("login-password").send_keys('invalid')
        self.browser.find_element_by_id("btn-submit").click()
        assert self.browser.find_elements_by_xpath("//*[contains(text(), 'Invalid email or password')]"),\
            "Expected error message (Invalid email or password) is not displayed."

    def test_click_on_submit_no_credentials(self):
        self.browser.find_element_by_id("btn-submit").click()
        assert self.browser.find_elements_by_xpath(
            "//*[contains(text(), 'Please enter a valid email address and password')]"),\
            "Expected error message (Please enter a valid email address and password) is not displayed."

    def test_empty_password_field(self):
        self.browser.find_element_by_id("login-email").send_keys(self.driver.email)
        self.browser.find_element_by_id("btn-submit").click()
        assert self.browser.find_elements_by_xpath(
            "//*[contains(text(), 'Please enter a valid email address and password')]"),\
            "Expected error message (Please enter a valid email address and password) is not displayed."
