from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app


    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, value="groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, value="new").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, value="submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element(By.NAME, value=field_name).click()
            driver.find_element(By.NAME, value=field_name).clear()
            driver.find_element(By.NAME, value=field_name).send_keys(text)

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element(By.NAME, value="delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, value="selected[]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        driver.find_element(By.NAME, value='edit').click()
        # fill group form
        self.fill_group_form(group=new_group_data)
        # submit modification
        driver.find_element(By.NAME, value='update').click()
        self.return_to_groups_page()



    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, value="group page").click()