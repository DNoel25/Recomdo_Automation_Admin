import pytest
from Pages.sidebar_page import SidebarPage

@pytest.mark.usefixtures("setup")
class TestSidebarNavigation:
    def test_navigate_to_module1(self):
        sidebar = SidebarPage(self.driver)
        sidebar.navigate_to_module1()

    def test_navigate_to_module2(self):
        sidebar = SidebarPage(self.driver)
        sidebar.navigate_to_module2()
