from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, value="group page").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, value="new").click()
        driver.find_element(By.NAME, value="group_name").click()
        driver.find_element(By.NAME, value="group_name").clear()
        driver.find_element(By.NAME, value="group_name").send_keys(group.name)
        driver.find_element(By.NAME, value="group_header").click()
        driver.find_element(By.NAME, value="group_header").clear()
        driver.find_element(By.NAME, value="group_header").send_keys(group.header)
        driver.find_element(By.NAME, value="group_footer").click()
        driver.find_element(By.NAME, value="group_footer").clear()
        driver.find_element(By.NAME, value="group_footer").send_keys(group.footer)
        driver.find_element(By.NAME, value="submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, value="groups").click()