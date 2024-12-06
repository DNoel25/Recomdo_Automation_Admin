from Pages.sidebar_page import SideNavigationPage
from Pages.search_sort_and_filter_page import SearchSortAndFilter
from Utils.base import BaseTest
import time

# @pytest.mark.usefixtures("setup")
class TestSortAndFilter(BaseTest):
    try:
        @classmethod
        def setup_class(cls):
            super().setup_class()
            side_nav1 = SideNavigationPage(cls.driver)
            side_nav1.open_search_results_management()
            side_nav1.open_sort_and_filter()

        def test_heading_available(self): 
            search_sort_page = SearchSortAndFilter(self.driver)
            search_sort_page.is_advanced_sortandfilter_heading_there()
            assert search_sort_page, "Heading is not displayed." # Use the result for the assertion   
        
        def test_sort_and_filter(self):
            # Step 1: 
            advanced_sort_and_filter = SearchSortAndFilter(self.driver)
            # Step 2: Select the Store View
            store_view = "English"   
            advanced_sort_and_filter.select_storeview(store_view)
            time.sleep(2) 

            # Step 2: Select the Sort By in Layered Navigation
            sort_by_option = "Select only selected attributes in order"
            # sort_by_option = "Select all attributes"
            advanced_sort_and_filter.select_sort_option_layered(sort_by_option)
            time.sleep(2)
  
            # Search in the grid
            if advanced_sort_and_filter.search_in_assign_box("age"):
                advanced_sort_and_filter.enter_15_in_searched_field("Age")  # Enter 15 if the attribute is found
                # Step 3: Save the changes
                advanced_sort_and_filter.save_changes()
                time.sleep(2)
            advanced_sort_and_filter.search_in_unassign_box("age")

            # Add assertions for verifying search results in the grid
            

        





        #     add_new_page.submit_form()
        #     print("cliecked the submit")
        #     time.sleep(10)
        # assert add_new_page.verify_success_message(), "Success message not displayed or incorrect." 

    except Exception as e:
            logging.error(f"Error in connection {e}") 