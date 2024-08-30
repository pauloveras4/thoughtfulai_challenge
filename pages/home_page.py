import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import HomePageLocators

from pages.base_page import BasePage


logger = logging.getLogger(__name__)

class HomePage(BasePage):
    """
    Class for the home page, ie. the first page which appears.
    
    Attributes
    ----------
    selenium : SeleniumLibrary
        instance of SeleniumLibrary which will be used in this page
    """
    
    def __init__(self, selenium):
       self.selenium = selenium

    def click_search_bar_icon(self):
        logger.info("Clicking search bar icon.")
        try:
            search_bar_icon_exists = self.selenium.is_element_enabled(
                HomePageLocators.HOME_PAGE_SEARCH_BAR_ICON_LOCATOR
            )
            if search_bar_icon_exists:
               logging.info("Search bar icon exists, clicking it...") 
               self.selenium.click_element_if_visible(
                    HomePageLocators.HOME_PAGE_SEARCH_BAR_ICON_LOCATOR
                )
               return 0
            return 1
        except:
            logger.error("Failed to click search bar icon.")
            return 2
    
    def enter_search_text(self, search_text):
        logger.info("Typing text into search bar")
        try:
            search_bar_input_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH, 
                        HomePageLocators.HOME_PAGE_SEARCH_BAR_INPUT_LOCATOR)
                    )
                )
            
            self.selenium.input_text_when_element_is_visible(
                HomePageLocators.HOME_PAGE_SEARCH_BAR_INPUT_LOCATOR,
                    search_text)
            search_bar_input_element.send_keys(Keys.ENTER)
            return 0
        except Exception as e:
            logger.error("Failed to find or type search text into searchbar.")
            return 1
    
    