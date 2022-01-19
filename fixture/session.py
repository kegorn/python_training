from selenium.webdriver.common.by import By


class SessionHelper():
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element(By.NAME, value="user").click()
        driver.find_element(By.NAME, value="user").clear()
        driver.find_element(By.NAME, value="user").send_keys(username)
        driver.find_element(By.NAME, value="pass").click()
        driver.find_element(By.NAME, value="pass").clear()
        driver.find_element(By.NAME, value="pass").send_keys(password)
        driver.find_element(By.XPATH, value='//*[@id="LoginForm"]/input[3]').click()

    def logout(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, value="Logout").click()

    def ensure_logout(self):
        # check that logout link is present
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements(By.LINK_TEXT, value="Logout")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return driver.find_element(By.XPATH, value="//div/div[1]/form/b").text == f"({username})"

    def ensure_login(self, username, password):
        driver = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username=username, password=password)