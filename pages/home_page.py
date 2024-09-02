import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from elements.element import BasePageElement
from locators.home_page_locators import HomePageLocators

from pages.base_page import BasePage


logger = logging.getLogger(__name__)

class SearchBarIconButtonElement(BasePageElement):
    """
    This class finds the element for the search bar icon which will be clicked so the modal appears. 
    
    Attributes
    ----------
    locator : By
        locator for the element which will be clicked
    """
    
    def __init__(self, selenium):
        super()
        self.selenium = selenium
        
    # The locator for the search bar icon button which will be clicked
    locator = HomePageLocators.HOME_PAGE_SEARCH_BAR_ICON_LOCATOR
    
class SearchBarInputElement(BasePageElement):
    """
    This class finds the element for the search bar input in which the search query will be inserted.
    
    Attributes
    ----------
    locator : By
        locator for the element which will store the input value
    """
    
    def __init__(self, selenium):
        super()
        self.selenium = selenium
    
    locator = HomePageLocators.HOME_PAGE_SEARCH_BAR_INPUT_LOCATOR
    
    
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
       self.wait = WebDriverWait(selenium.driver, 10)

    def click_search_bar_icon(self):
        logger.info("Clicking search bar icon.")
        try:
            search_bar_icon_element = SearchBarIconButtonElement(self.selenium)
            logger.info("Waiting for SearchBarIconButtonElement to appear...")
            search_bar_icon_element.__wait__()
            logger.info("Clicking SearchBarIconButtonElement...")
            search_bar_icon_element.__click__()
            logger.info("Clicked SearchBarIconButtonElement successfully! :D")
            return 0
        except Exception as e:
            logger.error("Failed to click search bar icon.")
            return 2
    
    def enter_search_query(self, search_query):
        logger.info("Typing text into search bar")
        try:
            search_bar_input_element = SearchBarInputElement(self.selenium)
            logger.info("Waiting for SearchBarInputElement to appear...")
            search_bar_input_element.__wait__()
            logger.info("Inserting text into SearchBarInputElement")
            search_bar_input_element.__set__(search_query)
            logger.info("Inserted text into SearchBarInputElement successfully! :D")
            logger.info("Pressing ENTER to go to results page")
            search_bar_input_element.__send_key__(Keys.ENTER)             
        except Exception as e:
            logger.error("Failed to find or type search text into searchbar.")
            return 1
    
    