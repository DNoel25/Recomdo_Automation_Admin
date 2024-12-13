# Pages/locators.py

from selenium.webdriver.common.by import By

class Locators:
#Search Results Management Module
    SEARCH_RESULTS_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
    MANUAL_SUGGESTION_SUBMODULE = ((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))
    # SEARCH_SORT_AND_FILTER = (By.XPATH, '//a[contains(text(), "Advanced Sort & Filter")]')
    SEARCH_SORT_AND_FILTER = (By.XPATH, '/html/body/div/aside/div/nav/ul/li[4]/ul/li[2]/a')


    # SEARCH_SORT_AND_FILTER = ((By.XPATH, '//a[contains(text(), "Advanced Sort & Filter")]'))
    
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


    #Locators for Advanced Sort & Filter
    ASF_STORE_VIEW_DROPDOWN = (By.XPATH, "//select[@name='store_view_select' and @id='store_view_select']")
    ASF_SORTOPTION_LAYERED = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[1]/div[2]/select")
    ASF_SAVE_BUTTON = (By.XPATH, "//button[@id='save_attribute_sort']")
    ASF_SEARCH_TEXT = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[2]/div[2]/div/div[1]/div[1]/input")
    ASF_UNASSIGNED_LIST = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[2]/div[2]/div/div[1]/div[2]/ul")
    #Locators for Sort By Options
    ASF_SORTOPTION_SORTBY = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[3]/div[2]/section/div/div[1]/div[2]/select")
    
#Category Management
    CATEGORY_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-tasks")])[1]'))
    LAYERED_NAVIGATION_SUBMODULE = ((By.XPATH, '//a[contains(text(), "Layered Navigation Sorting")]'))

    EXPAND_ALL = ((By.XPATH, '//*[@id="expand_all"]'))
    COLLAPSE_ALL = ((By.XPATH, '//*[@id="collapse_all"]'))
    CM_STORE_VIEW_DROPDOWN = (By.XPATH, "//select[@name='store_view_select' and @id='store_view_select']")
    CM_SORTOPTION_LAYERED = (By.XPATH, "/html/body/div[1]/div[1]/section[2]/div[2]/div/div[2]/div/div/div[2]/div[3]/div[1]/div[2]/select")
    CM_SAVE_BUTTON = (By.XPATH, "//button[@id='save_category_attribute_sort']")
    CM_SEARCH_TEXT = (By.XPATH, "/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/div/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/input")
    CM_UNASSIGNED_LIST = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[2]/div[2]/section/div/div[2]/div[2]/div/div[1]/div[2]/ul")
    
    #Locators for Sort By Options
    ASF_SORTOPTION_SORTBY = (By.XPATH, "/html/body/div/div[1]/section[2]/div[2]/div/div/div/div[3]/div[2]/section/div/div[1]/div[2]/select")

    #Locators for Grid view
    CM_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@id='products-per-page']"))  # Dropdown for entries shown per page
    # CM_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='SuggestionTable_length' and @aria-controls='SuggestionTable']"))  # Dropdown for entries shown per page 
    CM_SAVE_BUTTON_IN_CATEGORY_GRID = (By.XPATH, "//button[@id='save_product_sort']")


#Report Management 
    RM_REPORT_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-book")])[1]')) 
    RM_SEARCH_TERMS_SUBMODULE = (By.XPATH, '//a[@href="/client-admin/report/search-terms/"]')
    RM_SHOW_ENTRIES_DROPDOWN = ((By.XPATH, "//select[@name='searchTermsTable_length' and @aria-controls='searchTermsTable']"))  # Dropdown for entries shown per page
    RM_SEARCH_FIELD = (By.ID, "searchTermsTable_filter")  # Search filter field
