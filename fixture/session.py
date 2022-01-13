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
