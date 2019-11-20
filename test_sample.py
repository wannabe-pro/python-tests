import unittest
from selenium.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class TestSample(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver('http://localhost:4444/wd/hub', 'chrome', 'ANY')

    def test_sample(self):
        driver = self.driver
        driver.get("http://nginx")
        self.assertIn("Welcome to nginx!", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
