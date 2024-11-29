# Pages/locators.py

from selenium.webdriver.common.by import By

class Locators:
    SEARCH_RESULTS_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
    MANUAL_SUGGESTION_SUBMODULE = ((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))
    
    #--- Manual Suggestions Page locators ---#
    Heading = (By.TAG_NAME, "h2")
    GRID_VIEW = (By.ID, "SuggestionTable_wrapper")  # Grid view element ID
    SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='SuggestionTable_length' and @aria-controls='SuggestionTable']"))  # Dropdown for entries shown per page
    SEARCH_FIELD = (By.ID, "search")  # Search filter field
    GRID_ACTIONS_COLUMN = (By.CSS_SELECTOR, ".grid-actions")  # Actions column in the grid 
    EDIT_BUTTON = (By.XPATH, "(//a[@title='Edit'])[1]")  # Edit button selector for the first row in the grid
    DELETE_BUTTON = (By.CSS_SELECTOR, ".delete-action")  # Delete button selector in grid
    STORE_VIEW_DROPDOWN = ((By.XPATH, "//select")) 
    # Add New Form Locators
     # Locators for form fields
    ADD_NEW_BUTTON = (By.ID, "add_suggestion")  # Add new manual suggestion button
    STORE_VIEW_DROPDOWN = (By.XPATH, "//select[@name='store_view' and @id='store_view_select']")  # Update with actual name
    KEYWORD_FIELD = (By.NAME, "old_search_keyword")  # Update with actual name
    SYNONYM_FIELD = (By.XPATH, "//input[@class='synonyms_field synonyms_field_default bg-white-50 border border-gray-300 rounded-lg']")  # Update if different
    WEIGHT_FIELD = (By.XPATH, "//input[@id='weight_field_id']")  # Update if different
    SAVE_BUTTON = (By.XPATH, "//button[@id='save_suggestion_data']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    #SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success') and contains(text(), 'Data Added successfully!')]")
