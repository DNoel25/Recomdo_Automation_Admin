# Pages/manual_suggestions_page.py


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators

class ManualSuggestionsPage:
    def __init__(self, driver):
        self.driver = driver

    
    def is_grid_displayed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.GRID_VIEW)
        )

     
    def search_in_grid(self, text):
        search_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(Locators.SEARCH_FIELD)
        )
        search_field.clear()
        search_field.send_keys(text)


    def set_show_entries(self, value):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.SHOW_ENTRIES_DROPDOWN)
        )
        dropdown.select_by_visible_text(value)

    def click_add_new(self):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.ADD_NEW_BUTTON)
        )
        add_button.click()

    def click_edit_button(self, row_index=0):
        edit_buttons = self.driver.find_elements(*Locators.EDIT_BUTTON)
        edit_buttons[row_index].click()


    def click_delete_button(self, row_index=0):
        delete_buttons = self.driver.find_elements(*Locators.DELETE_BUTTON)
        delete_buttons[row_index].click()

    def my name
    