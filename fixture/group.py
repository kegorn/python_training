from selenium.webdriver.common.by import By


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/groups.php") and len(driver.find_elements(By.NAME, value="new")) > 0):
            driver.find_element(By.LINK_TEXT, value="groups").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, value="new").click()
        self.fill_group_form(group)
        driver.find_element(By.NAME, value="submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
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
        self.edit_selected_group()
        # fill group form
        self.fill_group_form(group=new_group_data)
        # submit modification
        driver.find_element(By.NAME, value='update').click()
        self.return_to_groups_page()

    def edit_selected_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, value='edit').click()

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, value="group page").click()

    def count_groups(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements(By.NAME, value="selected[]"))

    def check_first_group(self, group):
        self.open_groups_page()
        self.select_first_group()
        self.edit_selected_group()
        self.verifiy_field_value("group_name", group.name)
        self.verifiy_field_value("group_header", group.header)
        self.verifiy_field_value("group_footer", group.footer)

    def verifiy_field_value(self, field_name, field_text):
        driver = self.app.driver
        if field_text is not None:
            return driver.find_element(By.NAME, value=field_name).get_attribute("value") == field_text
        #return False



