import unittest


from EnvironmentBase.EnvironmentBase import EnvironmentBase


class MyTestCase(EnvironmentBase):

    def testBase(self):
        driver = self.driver
        driver.get("https://www.google.com")



if __name__ == '__main__':
    unittest.main()
