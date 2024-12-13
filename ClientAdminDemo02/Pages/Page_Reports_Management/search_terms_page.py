from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators   
import logging
import time

class SearchTermsPage:
    def __init__(self, driver):
        self.driver = driver
    
    def is_search_terms_heading_there(self):
        time.sleep(5)
        print("1")
        try:
            print("2")
            headig = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@class='text-5xl font-extrabold dark:text-white' and contains(., 'Search Terms')]"))
            )
            print("Search Terms Heading is there")
            time.sleep(2)
            return heading.is_displayed()
        
        except Exception as e:
            logging.error(f"Error locating Search Terms heading: {e}")
            return False

    def is_grid_displayed(self):
        try:
            grid = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//table[@id='searchTermsTable']"))
            )
            print("Search Terms grid is there")
            return grid.is_displayed()
        
        except Exception as e:
            logging.error(f"Error locating grid element: {e}")
            return false

    def set_show_entries(self, value):
        time.sleep(5)
        try:
            print(f"Setting show entries to {value}")
            
            # Locate the dropdown element and create a Select object
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.RM_SHOW_ENTRIES_DROPDOWN)
            )
            select = Select(dropdown_element)
            
            # Select the desired option in the dropdown
            select.select_by_visible_text(str(value))
            print(f"Dropdown set to {value}")

            # Wait until the grid is updated by checking the number of rows
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//table[@id='searchTermsTable']/tbody/tr")) <= int(value)
            )
            
            # Fetch the updated rows after setting the dropdown
            rows = self.driver.find_elements(By.XPATH, "//table[@id='searchTermsTable']/tbody/tr")
            actual_count = len(rows)
            
            # Debug print to confirm actual count
            print(f"Expected up to {value} entries, found {actual_count} entries in the grid.")

            # Verify if the number of rows is equal to the selected dropdown value or less
            assert actual_count == int(value) or actual_count < int(value), f"Expected up to {value} entries, but found {actual_count}."
            
        except Exception as e:
            logging.error(f"Error in setting show entries dropdown: {e}")
            return False
        return True

    def search_in_grid(self, text): 
        try:
            # Locate and clear the search field, then enter the search text
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-controls='searchTermsTable']"))
            ) 
            search_field.clear()
            search_field.send_keys(text)
            print(f"Searching for '{text}' in the grid...")

            # Wait for the search results to be displayed in the grid
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//table[@id='searchTermsTable']/tbody/tr"))
            ) 
            time.sleep(2)
            # Fetch all rows in the grid
            rows = self.driver.find_elements(By.XPATH, "//table[@id='searchTermsTable']/tbody/tr")

            # Check if any cell in any row contains the search text
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                for cell in cells:
                    if text.lower() in cell.text.lower():  # Case-insensitive match
                        print(f"Found '{text}' in grid cell with text: '{cell.text}'")
                        time.sleep(2)
                        search_field.clear()
                        self.driver.refresh()
                        time.sleep(2)
                        return True  # Return True if a match is found
            print(f"No match found for '{text}' in the grid.")
            return False  # Return False if no match is found in any cell

        except Exception as e:
            logging.error(f"Error during search in grid: {e}")
            return False