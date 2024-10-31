# ClientAdminDemo02/Tests/test_manual_suggestions.py

import pytest
from Pages.login_page import LoginPage
from haha.manual_suggestions import ManualSuggestionsPage
from Utils.base import BaseTest
# from Tests.test_login import TestLogin

class TestManualSuggestions(BaseTest):
    def test_manual_suggestions_grid(self): 
        # login handling is doing by the base.py
        

        # Navigate to Manual Suggestions
        manual_suggestions_page = ManualSuggestionsPage(self.driver)
        manual_suggestions_page.realtimesync()
    
        # # Check if the grid is displayed
        # assert manual_suggestions_page.is_grid_displayed(), "Manual Suggestions grid is not displayed"
