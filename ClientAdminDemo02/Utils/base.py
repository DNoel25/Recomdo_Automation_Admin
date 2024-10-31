from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


from Pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class BaseTest:
    pass

class BaseTest:
    def setup_method(self):
        driver_path = r"C:\Users\neosolax\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://demoapi2.recomdo.ai/client-admin")
        self.driver.maximize_window()
        login_page = LoginPage(self.driver) 
        login_page.login("abans_client", "Porsche9000#")

    def teardown_method(self):
        self.driver.quit()


