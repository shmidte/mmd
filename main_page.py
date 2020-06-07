from basepage import BasePage
from selenium.webdriver.common.by import By


class TODOLocators:
    LOCATOR_TODO_FIELD = (By.ID, 'new-todo')
    LOCATOR_CREATED_TODO = (By.XPATH, '/html/body/div/section/section/ul/li/div/label')

class SearchHelper(BasePage):

    def enter_word(self, word):
        todo_field = self.find_element(TODOLocators.LOCATOR_TODO_FIELD)
        todo_field.click()
        todo_field.send_keys(word)
        return todo_field

    def create_todo(self):
        return self.find_element(TODOLocators.LOCATOR_TODO_FIELD,time=2).send_keys(u'\ue007')

    def check_created_todo(self):
        todo_label = self.find_element(TODOLocators.LOCATOR_CREATED_TODO)
        name_label = todo_label.text
        return name_label


