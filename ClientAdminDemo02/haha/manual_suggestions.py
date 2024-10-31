# ClientAdminDemo02/Pages/manual_suggestions_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ManualSuggestionsPage:
    def __init__(self, driver):
        self.driver = driver

    def realtimesync(self):
        # Assuming there's a side navigation element to click on
        # dashboard_button  = WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="button"]'))
        # )
        # dashboard_button.click()
        print("real time sync btn clicked")
        WebDriverWait(self.driver, 20)
    # def navigate_to_manual_suggestions(self):
    #     # Assuming there's a side navigation element to click on
    #     manual_suggestions_link1 = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.CLASS_NAME, "nav-icon fas fa-poll-h"))
    #     )
    #     manual_suggestions_link1.click()

    # def is_grid_displayed(self):
    #     # Adjust the selector to match the grid's unique identifier
    #     return WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.ID, "manual-suggestions-grid"))
    #     )
