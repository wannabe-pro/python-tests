import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            esired_capabilities=webdriver.DesiredCapabilities.CHROME,
            command_executor='http://localhost:4444/wd/hub'
        )

    def test_sample(self):
        driver = self.driver
        driver.get("http://nginx")
        self.assertIn("Welcome to nginx!", driver.title)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
