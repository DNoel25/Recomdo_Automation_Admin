# Pages/locators.py

from selenium.webdriver.common.by import By

class Locators:
    SEARCH_RESULTS_MANAGEMENT_MENU = ((By.XPATH, '(//i[contains(@class, "nav-icon fas fa-search")])[1]'))
    MANUAL_SUGGESTION_SUBMODULE = ((By.XPATH, '//a[contains(text(), "Manual Suggestions")]'))

    # Manual Suggestions Page locators
    GRID_VIEW = (By.ID, "SuggestionTable")  # Grid view element ID
    SHOW_ENTRIES_DROPDOWN = (By.NAME, "SuggestionTable_length")  # Dropdown for entries shown per page
    SEARCH_FIELD = (By.ID, "search")  # Search filter field
    GRID_ACTIONS_COLUMN = (By.CSS_SELECTOR, ".grid-actions")  # Actions column in the grid
    ADD_NEW_BUTTON = (By.ID, "add_suggestion")  # Add new manual suggestion button
    EDIT_BUTTON = (By.CSS_SELECTOR, ".edit-action")  # Edit button selector in grid
    DELETE_BUTTON = (By.CSS_SELECTOR, ".delete-action")  # Delete button selector in grid
