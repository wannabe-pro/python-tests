import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

"""
Пример теста.
Вcе тесты запускаются из файлов вида test_*.py или *_test.py.
Перед выполнение тестов надо поднять контейнеры с сервисами selenium и nginx.
"""


class TestSample(unittest.TestCase):

    def setUp(self):
        """
        Инициализация теста, делаем соединение с selenium.
        """
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def test_sample(self):
        """
        Простой тест, переходим на страницу приметствия nginx и проверяем заголовок.
        """
        driver = self.driver
        driver.get('http://nginx')
        self.assertIn('Welcome to nginx!', driver.title)

    def tearDown(self):
        """
        Деструктор теста, убиваем соединение с selenium.
        """
        self.driver.close()


# для совместимости с unittest
if __name__ == '__main__':
    unittest.main()
