# Tests/test_manual_suggestions.py

import pytest
from Pages.sidebar_page import SideNavigationPage
from Utils.base import BaseTest 
from Pages.manual_suggestions_page import ManualSuggestionsPage
from Pages.sidebar_page import SideNavigationPage
from Utils.base import BaseTest

class TestManualSuggestions(BaseTest):

    # Tests/test_manual_suggestions.py 
    def setup_method(self):
        super().setup_method()
        # Instantiate the SideNavigationPage
        side_nav = SideNavigationPage(self.driver)
        # Navigate to "Search Results Management" and then to "Manual Suggestions"
        side_nav.open_search_results_management()
        side_nav.open_manual_suggestions()
        # Verify that the Manual Suggestions page is displayed
        # You can add assertions based on page elements to confirm successful navigation
        assert "Manual Suggestions" in self.driver.title

    # @pytest.mark.order(1)
    def test_grid_displayed(self):
        manual_page = ManualSuggestionsPage(self.driver)
        assert manual_page.is_grid_displayed(), "Grid is not displayed on Manual Suggestions page."

    # def test_show_entries(self):
    #     manual_page = ManualSuggestionsPage(self.driver)
    #     manual_page.set_show_entries("50")  # Adjust value as per dropdown options
    #     # Add assertions based on expected number of items per page, if accessible

    # def test_search_functionality(self):
    #     manual_page = ManualSuggestionsPage(self.driver)
    #     manual_page.search_in_grid("Test")
    #     # Add assertions for verifying search results in the grid

    # def test_add_new_suggestion(self):
    #     manual_page = ManualSuggestionsPage(self.driver)
    #     manual_page.click_add_new()
    #     # Add assertions to verify new suggestion form is displayed

    # def test_edit_suggestion(self):
    #     manual_page = ManualSuggestionsPage(self.driver)
    #     manual_page.click_edit_button()
    #     # Add assertions to verify edit modal or form is displayed

    # def test_delete_suggestion(self):
    #     manual_page = ManualSuggestionsPage(self.driver)
    #     manual_page.click_delete_button()
    #     # Add assertions to verify deletion success, such as confirmation modal or grid update

