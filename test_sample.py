import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor = 'http://127.0.0.1:4444/wd/hub',
            desired_capabilities = DesiredCapabilities.CHROME
        )

    def test_sample(self):
        driver = self.driver
        driver.get("http://nginx")
        self.assertIn("Welcome to nginx!", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
