from selenium.webdriver.common.by import By


class ContactHelper():
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, value="add new").click()

    def create(self, contact):
        driver = self.app.driver
        self.open_contact_page()
        driver.find_element(By.NAME, value="firstname").click()
        driver.find_element(By.NAME, value="firstname").clear()
        driver.find_element(By.NAME, value="firstname").send_keys(contact.firstname)
        driver.find_element(By.NAME, value="lastname").click()
        driver.find_element(By.NAME, value="lastname").clear()
        driver.find_element(By.NAME, value="lastname").send_keys(contact.lastname)
        driver.find_element(By.NAME, value="address2").click()
        driver.find_element(By.NAME, value="address2").clear()
        driver.find_element(By.NAME, value="address2").send_keys(contact.address2)
        driver.find_element(By.NAME, value="submit").click()
        self.app.open_home_page()
