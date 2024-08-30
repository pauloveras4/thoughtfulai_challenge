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
            logger.info("Verifying section filter dropdown exists...")
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
            logger.fatal("Unable to find or click section filter dropdown...")
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

    def _click_sort_by_order_dropdown(self):
        logger.info("Clicking sort by dropdown.")
        try:
            logger.info("Verifying sort by dropdown exists...")
            
            sort_by_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        ResultsPageLocators.RESULTS_PAGE_SORT_BY_SELECT_BUTTON_LOCATOR
                    )
                )
            )
            
            sort_by_element.click()
            return 0
        except Exception as e:
            logger.fatal("Unable to find or click sort by dropdown...")
            return 1
 
    def select_sort_by_order_from_dropdown(self, order):
        logger.info("Selecting sort by order from dropdown.")
        try:
            self._click_sort_by_order_dropdown()
        
            sort_by_item_element_locator = ResultsPageLocators.RESULTS_PAGE_SORT_BY_SELECT_ITEM_LOCATOR(order)
            
            sort_by_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,                        
                        sort_by_item_element_locator 
                    )        
                )
            )
        
            sort_by_element.click()
            logger.info("Selected order successfully! :)")
            return 0
        except Exception as e:
            logger.fatal("Unable to find or select sort by order from dropdown")
            return 1
    
    def _get_current_heading(self, current_index_str):
        try:
            heading_element_locator = ResultsPageLocators.RESULT_ITEM_HEADING_LOCATOR(current_index_str)
            
            heading_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                    By.XPATH,
                    heading_element_locator
                    ) 
                )
            )
            
            heading = heading_element.text
            
            return heading 
        except Exception as e:
            logger.fatal("Unable to find current news heading") 
   
    def _get_current_date(self, current_index_str):
        try:
            date_element_locator = ResultsPageLocators.RESULT_ITEM_DATE_LOCATOR(current_index_str)
            
            date_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                    By.XPATH,
                    date_element_locator 
                    ) 
                )
            )
            
            date = date_element.get_attribute("textContent")
            
            return date 
        except Exception as e:
            logger.fatal("Unable to find current news heading") 
    
    def iter_through_current_news(self, index_current_item):
        logger.info("Iterating through current news.")
        current_index_str = str(index_current_item)
        try:
            heading = self._get_current_heading(current_index_str)
            date = self._get_current_date(current_index_str)
            print(heading)
            print(date)
        except Exception as e:
            logger.fatal("Unable to find current news item")
        
        
        
        

