import unittest
from selenium import webdriver


class EnvironmentBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/rahulsingh/Desktop/MyComputer/Automation/Drivers/chromedriver")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
