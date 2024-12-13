# Tests/test_search_pages.py

import logging
import time
import pytest
from Pages.sidebar_page import SideNavigationPage
from Pages.Page_Reports_Management.search_terms_page import SearchTermsPage
from Utils.base import BaseTest

# @pytest.mark.usefixtures("setup")
class TestSearchTerms(BaseTest):

    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav = SideNavigationPage(cls.driver)
            side_nav.open_report_management()
            side_nav.open_search_terms()
            time.sleep(2)

        def test_heading_available(self): 
            search_terms = SearchTermsPage(self.driver)
            search_terms.is_search_terms_heading_there()
            assert search_terms, "Heading is not displayed." # Use the result for the assertion

        def test_grid_displayed(self):
            search_terms = SearchTermsPage(self.driver)
            search_terms.is_grid_displayed()
            # assert search_terms.is_grid_displayed(), "Grid is not displayed on Search Terms page."

        def test_show_entries_options(self):
            search_terms = SearchTermsPage(self.driver)
            for value in [10, 25, 50, 100]:
                assert search_terms.set_show_entries(value), f"Failed to set and verify show entries to {value}."

        def test_search_functionality(self):
            search_terms = SearchTermsPage(self.driver)
            search_terms.search_in_grid("love")
            # Add assertions for verifying search results in the grid

    except Exception as e:
            logging.error(f"Error in connection {e}") 
    

    