from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException


class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.groupHelper = GroupHelper(self)
        self.contactHelper = ContactHelper(self)
        # self.base_url = "https://www.google.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.driver.quit()
    # self.assertEqual([], self.verificationErrors)

        # def is_element_present(self, how, what):
        #     try:
        #         self.driver.find_element(by=how, value=what)
        #     except NoSuchElementException as e:
        #         return False
        #     return True
        #
        # def is_alert_present(self):
        #     try:
        #         self.driver.switch_to_alert()
        #     except NoAlertPresentException as e:
        #         return False
        #     return True
        #
        # def close_alert_and_get_its_text(self):
        #     try:
        #         alert = self.driver.switch_to_alert()
        #         alert_text = alert.text
        #         if self.accept_next_alert:
        #             alert.accept()
        #         else:
        #             alert.dismiss()
        #         return alert_text
        #     finally:
        #         self.accept_next_alert = True


