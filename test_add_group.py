# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_test_add_group(self):
        driver = self.driver

        self.open_home_page(driver)

        self.login(driver)

        self.open_groups_page(driver)

        self.create_group(driver)

        self.return_to_groups_page(driver)

        self.logout(driver)

    def logout(self, driver):
        driver.find_element(By.LINK_TEXT, value="Logout").click()

    def return_to_groups_page(self, driver):
        driver.find_element(By.LINK_TEXT, value="group page").click()

    def create_group(self, driver):
        driver.find_element(By.NAME, value="new").click()
        driver.find_element(By.NAME, value="group_name").click()
        driver.find_element(By.NAME, value="group_name").clear()
        driver.find_element(By.NAME, value="group_name").send_keys("new_group1")
        driver.find_element(By.NAME, value="group_header").click()
        driver.find_element(By.NAME, value="group_header").clear()
        driver.find_element(By.NAME, value="group_header").send_keys("new_group1")
        driver.find_element(By.NAME, value="group_footer").click()
        driver.find_element(By.NAME, value="group_footer").clear()
        driver.find_element(By.NAME, value="group_footer").send_keys("new_group1")
        driver.find_element(By.NAME, value="submit").click()

    def open_groups_page(self, driver):
        driver.find_element(By.LINK_TEXT, value="groups").click()

    def login(self, driver):
        driver.find_element(By.NAME, value="user").click()
        driver.find_element(By.NAME, value="user").clear()
        driver.find_element(By.NAME, value="user").send_keys("admin")
        driver.find_element(By.NAME, value="pass").click()
        driver.find_element(By.NAME, value="pass").clear()
        driver.find_element(By.NAME, value="pass").send_keys("secret")
        driver.find_element(By.XPATH, value='//*[@id="LoginForm"]/input[3]').click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
