# Pages/manual_suggestions_page.py
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.locators import Locators   
import logging
import time


class LayeredNavigationPage:
    def __init__(self, driver):
        self.driver = driver
    
    def is_category_layered_navigation_heading_there(self): 
        try:
            heading = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@class='text-5xl font-extrabold dark:text-white' and contains(., 'Category Layered Navigation Sorting')]"))
            )
            print("Category Layered Nvagigation Heading is there")
            return heading.is_displayed()
        except Exception as e:
            logging.error(f"Error locating Category Layered Nvagigation heading: {e}")
            return False

    def click_expand_all(self):
        # Click the "Expand All" button 
        expand_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.EXPAND_ALL)
        )
        expand_button.click()
        time.sleep(2)
        # Verify that all 'details' elements have the open="open" attribute
        details_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="section2"]/div[3]/div[2]/ul/li/details'))
        )
        for details in details_elements:
            assert "open" in details.get_attribute("outerHTML"), "Details element is not expanded"


    def click_collapse_all(self):
        # Click the "Collapse All" button 
        collapse_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.COLLAPSE_ALL)
        )
        collapse_button.click()
        print("collapsed clicked")
        time.sleep(2)
        # Verify that no 'details' elements have the open="open" attribute
        details_elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="section2"]/div[3]/div[2]/ul/li/details'))
        )
        for details in details_elements:
            assert "open" not in details.get_attribute("outerHTML"), "Details element is not collapsed"
 
    def select_storeview(self, store):
        # Select store view from dropdown
        store_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.CM_STORE_VIEW_DROPDOWN)
        )
        Select(store_dropdown).select_by_visible_text(store)
        print("Successfully selected the store view!")

    def select_first_category(self):
        # Wait for the first <li> button in the category tree list to be clickable
        first_category_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.ml-4.border-l > li:first-of-type > button.category_name_button"))
        ) 
        # Click the first category button
        first_category_button.click()

        print("Clicked the first category in the tree") 
        

    def select_sort_option_layered(self, sortOption):
        # Select store view from dropdown 
        sort_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.CM_SORTOPTION_LAYERED)
        )
        sort_option.click()
        Select(sort_option).select_by_visible_text(sortOption)
        
        print("Successfully Selected the Sort By Option in Layered Navigation Section!")     
    
    # def select_sort_option_layered1(self, sortOption):
    #     # Select store view from dropdown 
    #     sort_option = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(Locators.CM_SORTOPTION_LAYERED)
    #     )
    #     sort_option.click()
    #     Select(sort_option).select_by_visible_text(sortOption)
        
    #     print("Successfully Selected the Sort By Option in Layered Navigation Section!")

    def save_changes(self):
        """
        Click the save button on top right cornor.
        """
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(Locators.CM_SAVE_BUTTON)
        )
        save_button.click()

    def search_in_assign_box(self, search_text):
        try:    
        #############################
            # If not found in unassigned list, search in assigned attributes list
            print(f"Searching for '{search_text}' in the assigned attributes list...")
            assigned_search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "search_assigned"))  # ID for the assigned search field
            )
            assigned_search_field.clear()
            assigned_search_field.send_keys(search_text)

            # # Wait for the search results to update in the assigned list
            # WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sortable-list.sort_unassigned-list .assigned_attribute_one"))
            # ) 

            # Fetch all filtered items in the assigned list
            assigned_items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.assigned-list .assigned_attribute_one")
            print(f"Got {len(assigned_items)} filtered items in the assigned attributes list.")

            # Verify if the searched text appears in any item of the assigned list
            for assigned_item in assigned_items:
                try:
                    # Find the span containing the attribute name within the current item
                    attribute_name_span = assigned_item.find_element(By.CLASS_NAME, "attribute_name")
                    assigned_item_text = attribute_name_span.text.strip()  # Extract text from the span

                    if search_text.lower() in assigned_item_text.lower():  # Partial case-insensitive match
                        print(f"Match found: '{search_text}' in assigned attribute: '{assigned_item_text}'")
                        time.sleep(5)
                        return True  # Return True if a match is found

                except Exception as e:
                    logging.error(f"Error processing assigned item: {e}")
                    continue

            print(f"'{search_text}' not found in the assigned attributes list.")
            return False  # Return False if no match is found in both lists


        except Exception as e:
            logging.error(f"Error during search in unassigned attributes box: {e}")
            return False
    
    def search_in_unassign_box(self, search_text):
        try:
            # Locate and clear the unassigned search field, then enter the search text
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(Locators.CM_SEARCH_TEXT)  # Assuming Locators.ASF_SEARCH_TEXT is By.ID("search_unassigned")
            )
            search_field.clear()
            search_field.send_keys(search_text)
            print(f"Searching for '{search_text}' in the unassigned attributes box...")

            # Wait for the search results to update in the unassigned list
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sortable-list.unassigned-list .unassigned_attribute_one"))  # Assuming Locators.ASF_UNASSIGNED_LIST is By.CSS_SELECTOR
            )

            # Fetch all filtered items in the unassigned list
            items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.unassigned-list .unassigned_attribute_one")
            print(f"Got {len(items)} filtered items in the unassigned attributes list.")

            # Verify if the searched text appears in any item of the unassigned list
            for item in items:
                try:
                    # Find the span containing the attribute name within the current item
                    attribute_name_span = item.find_element(By.CLASS_NAME, "attribute_name")
                    item_text = attribute_name_span.text.strip()  # Extract text from the span

                    if search_text.lower() in item_text.lower():  # Partial case-insensitive match
                        print(f"Match found: '{search_text}' in unassigned attribute: '{item_text}'")
                        time.sleep(5)
                        return True  # Return True if a match is found
                    

                except Exception as e:
                    logging.error(f"Error processing item: {e}")
                    continue

            print(f"'{search_text}' not found in the unassigned attributes list.")


        except Exception as e:
            logging.error(f"Error during search in unassigned attributes box: {e}")
            return False 
            
    def enter_1_in_searched_field(self, search_text):
        try:
            # Fetch all filtered items in the assigned list
            assigned_items = self.driver.find_elements(By.CSS_SELECTOR, ".sortable-list.assigned-list .assigned_attribute_one")
            print(f"Got {len(assigned_items)} filtered items in the assigned attributes listsss.")

            if (len(assigned_items)) > 1:
                # Locate the input field for the searched attribute (e.g., 'Age')
                input_field1 = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((
                        By.CSS_SELECTOR, 
                        f"li[id='{search_text}'] .number_div input[name='order_number_assigned']"
                    ))
                )
                
                # Clear the input field and type '1'
                input_field1.clear()
                input_field1.send_keys("1")
                print(f"Entered '1' in the searched field for '{search_text}'.")
                time.sleep(2)

                #Saving the changes
                self.save_changes() 
            
                # Optional: Wait for the page to refresh or changes to take effect
                WebDriverWait(self.driver, 10).until(EC.staleness_of(input_field1)) 
                # Step 4: Verify the updated value in the input field
                updated_input_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 
                        f"li[id='{search_text}'] .number_div input[name='order_number_assigned']"
                    ))
                )
  
                # Step 5: Retrieve the value and check if it is updated to '1'
                input_value = updated_input_field.get_attribute('value')
                if input_value == "1":
                    print("The keyword has been updated to 1 successfully.")
                else:
                    print(f"The keyword update failed. Current value: {input_value}")
                
            else:
                print("huhuhu not greater")
            
        except Exception as e:
            logging.error(f"Error during entering '16' in the searched field for '{search_text}': {e}")
            return False  # If an error occurs, return False

    def is_delete_button_visible_for_price(self):
        """
        Check if the delete button is visible for the 'Price' attribute in the assigned list.
        :return: True if the delete button is visible, False otherwise.
        """
        try:
            # Wait for the specific 'Price' attribute element in the assigned list
            price_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//li[@class='assigned_attribute_one' and @id='price']")
                )
            )
            print("Found the 'Price' attribute in the assigned list.")

            # Check if the delete button exists within this element
            delete_button = price_element.find_elements(By.CSS_SELECTOR, "button.delete-button")
            if not delete_button:
                print("Delete button is NOT visible for 'Price', as expected.")
                return True  # Delete button is visible
            else:
                print("Delete button is visible for 'Price'. This is unexpected.")
                return False  # Delete button is not visible
        except TimeoutException:
            print("Timed out waiting for the 'Price' attribute to load.")
            return False
        except NoSuchElementException as e:
            print(f"Error locating 'Price' attribute or its delete button: {e}")
            return False

    def enter_15_in_searched_field(self, search_text):
        try:
            # Locate the input field for the searched attribute (e.g., 'Age')
            input_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((
                    By.CSS_SELECTOR, 
                    f"li[id='{search_text}'] .number_div input[name='order_number_unassigned']"
                ))
            )
            
            # Clear the input field and type '16'
            input_field.clear()
            input_field.send_keys("15")
            print(f"Entered '15' in the searched field for '{search_text}'.")
            time.sleep(2)
            return True  # Successfully entered '16' in the field

        except Exception as e:
            logging.error(f"Error during entering '15' in the searched field for '{search_text}': {e}")
            return False  # If an error occurs, return False    


#Grid view testing
    def select_first_category1(self):
        # Wait for the first <li> button in the category tree list to be clickable
        first_category_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.ml-4.border-l > li:first-of-type > button.category_name_button"))
        )
        # Print the text of the category name
        category_name = first_category_button.text
        print(f"Category Name: {category_name}")
        # Click the first category button
        first_category_button.click()

        print("Clicked the first category in the tree")
        return category_name

    def redirect_gridview(self):  
        #&&&&need to test the name vs the heading in cateegory page&&&&
        # name = self.select_first_category1()
        # print(name)
        gridview_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@id='product_grid_sort_link' and contains(@class, 'text-white') and contains(text(), 'View Grid')]"))
        )
        gridview_btn.click()
        print("Successfully clicked the view grid btn")
 
    def set_show_entries(self, value):
        try:
            print(f"Setting show entries to {value}")
            
            # Locate the dropdown element and create a Select object
            dropdown_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.CM_SHOW_ENTRIES_DROPDOWN)
            )
            select = Select(dropdown_element)
            
            # Select the desired option in the dropdown
            select.select_by_visible_text(str(value))
            print(f"Dropdown set to {value}")

            time.sleep(10)
            # Wait until the grid updates by checking the number of visible grid items
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//div[@class='grid']/div[contains(@class, 'grid-item')]")) <= int(value)
            )
            
            # Fetch the updated grid items after setting the dropdown
            grid_items = self.driver.find_elements(By.XPATH, "//div[@class='grid']/div[contains(@class, 'grid-item')]")
            actual_count = len(grid_items)
            
            # Debug print to confirm actual count
            print(f"Expected up to {value} entries, found {actual_count} entries in the grid.")

            # Verify if the number of grid items is equal to the selected dropdown value or less
            assert actual_count == int(value) or actual_count < int(value), f"Expected up to {value} entries, but found {actual_count}."
            # Refresh the current page
            # self.driver.refresh()
            # time.sleept(1)
            
        except Exception as e:
            logging.error(f"Error in setting show entries dropdown: {e}")
            return False
        return True

    def search_in_grid(self, sku):
        try:
            # Locate and clear the search field, then enter the SKU
            search_field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="product-search"]'))
            )
            search_field.clear()
            search_field.send_keys(sku)
            print(f"Searching for SKU '{sku}' in the grid...")
            time.sleep(5)
            # Wait for the grid to update after search
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.find_elements(By.XPATH, "//div[contains(@class, 'grid-item')]")) > 0
            )

            # Locate the product grid items
            grid_items = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'grid-item')]")
            print(f"Found {len(grid_items)} items in the grid after search.")

            # Iterate through each grid item to find the matching SKU
            for item in grid_items:
                # Locate the SKU element within the grid item
                sku_element = item.find_element(By.XPATH, ".//p[contains(@class, 'grid-item-sku')]")
                grid_sku = sku_element.get_attribute("title").strip()  # Use the 'title' attribute for the SKU
                print(f"Checking SKU: '{grid_sku}'")

                # Check if the SKU matches the searched SKU
                if sku.lower() == grid_sku.lower():
                    print(f"Match found: '{grid_sku}' matches searched SKU '{sku}'")
                    time.sleept(4)
                    return True  # Return True if a match is found

            # If no matching SKU is found
            print(f"No match found for SKU '{sku}' in the grid.")
            return False

        except Exception as e:
            logging.error(f"Error during search in grid: {e}")
            return False





    