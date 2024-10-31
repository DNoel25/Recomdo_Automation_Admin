# Pages/side_navigation_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators

class SideNavigationPage:
    def __init__(self, driver):
        self.driver = driver

    def open_search_results_management(self):
        # Wait for and click on the "Search Results Management" main menu item by indexing
        search_results_management = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.SEARCH_RESULTS_MANAGEMENT_MENU)
        )
        search_results_management.click()
        print("Main menu item 'Search Results Management' clicked")

    def open_manual_suggestions(self):
        # Wait for and click on the "Manual Suggestions" submodule item by unique text or order
        manual_suggestions = WebDriverWait(self.driver, 10).until(
            # EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))
            # I pass this using the locatiors class
            EC.element_to_be_clickable(Locators.MANUAL_SUGGESTION_SUBMODULE)
        )
        manual_suggestions.click()
        print("Submodule 'Manual Suggestions' clicked")
