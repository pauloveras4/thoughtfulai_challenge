import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
        self.wait = WebDriverWait(self.selenium.driver, 10)

    def _click_section_filter_dropdown(self):
        logger.info("Clicking section filter dropdown.")
        try:
            logger.info("Verifying dropdown exists...")
            section_filter_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        ResultsPageLocators.RESULTS_PAGE_SECTION_SELECT_BUTTON_LOCATOR
                    )
                )
            )
            section_filter_element.click()
            return 0
        except Exception as e:
            logger.fatal("Unable to find or click dropdown...")
            return 1
        
    def select_section_filter_from_dropdown(self, section):
        logger.info("Selecting section filter from dropdown.")
        try:
            self._click_section_filter_dropdown()
            section_item_element_locator = ResultsPageLocators.RESULTS_PAGE_SECTION_SELECT_ITEM_LOCATOR(section)
            section_item_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,                        
                        section_item_element_locator
                    )        
                )
            )
            section_item_element.click()
            logger.info("Selected section successfully! :)")
            return 0
        except Exception as e:
            logger.fatal("Unable to find or select filter from dropdown")
            return 1
    