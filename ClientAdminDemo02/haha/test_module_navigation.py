# # Tests/test_inventory_management.py
# import pytest
# from selenium import webdriver
# from Pages.manual_suggestion import InventoryManagementPage 
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# class TestNavigation:
#     def setup_method(self):
#         # Setup code: Initialize WebDriver and log in
#         self.driver = ...  # Initialize your WebDriver
#         self.driver.get("https://demoapi2.recomdo.ai/client-admin")
#         self.login("abans_client", "Porsche9000#")  # Implement your login method

#     def teardown_method(self):
#         self.driver.quit()

#     def test_navigate_to_inventory_management(self):
#         self.driver.find_element(By.LINK_TEXT, "Search Result Management").click()
#         WebDriverWait(self.driver, 10).until(EC.title_contains("Search Result Management"))
#         assert "Inventory Management" in self.driver.title
