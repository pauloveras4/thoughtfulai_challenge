import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locators.results_page_locators import ResultsPageLocators

from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ResultsPage(BasePage):
    """
    Class for the results page, the page in which the final results
    from the query appear.
    
    Attributes
    ----------
    selenium: SeleniumLibrary
        instance of SeleniumLibrary which will be used in this page
    """
    
    def __init__(self, selenium):
        self.selenium = selenium
        
    