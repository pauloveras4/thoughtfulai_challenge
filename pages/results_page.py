import logging
import requests

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.results_page_locators import ResultsPageLocators
from pages.base_page import BasePage
from utils.date_parser import DateParser
from utils.currency_parser import CurrencyParser

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
        self.action = ActionChains(self.selenium.driver)

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
    
    def _get_current_image(self, current_index_str):
        try:
            image_element_locator = ResultsPageLocators.RESULT_ITEM_IMAGE_LOCATOR(current_index_str)
            
            image_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        image_element_locator
                    )
                )
            )
            
            return image_element.get_attribute('alt'), image_element.get_attribute('src')
        
        except Exception as e:
            logger.fatal("Unable to find current image")
    
    def _move_to_image(self, current_index_str):
        image_element = self.selenium.driver.find_element(
            By.XPATH,
            ResultsPageLocators \
                .RESULT_ITEM_IMAGE_LOCATOR(current_index_str)
        )
        self.selenium.driver.execute_script("arguments[0].scrollIntoView(true);", image_element)
        self.action \
            .move_to_element(image_element) \
            .perform()
    
    def _download_image(image_source, image_filename):
        response = requests.get(image_source)
        
        if response.status_code == 200:
            with open(f"./output/{image_filename}", "wb") as file:
                file.write(response.content)
        
        
    def _iter_through_current_news(self, index_current_item, search_query):
        logger.info("Iterating through current news.")
        current_index_str = str(index_current_item)
        try:
            title = self._get_current_heading(current_index_str)
            
            date = self._get_current_date(current_index_str)
            date = DateParser(date).parse_date_to_proper_string()
            
            image = self._get_current_image(current_index_str)
            
            # Scrolls down to find more images
            if (index_current_item) % 7 == 0:
                self._move_to_image(current_index_str)

            image_source = image[1]
            image_filename =  f"{image[0]}.jpg"
            
            self._download_image(image_source, image_filename)
            
            search_query_count = title.count(search_query)
            
            currency_in_title = CurrencyParser(title).verifies_title_contains_currency()
                       
            return {
                'title': title, 
                'date': date, 
                'filename_image': image_filename, 
                'search_query_count': search_query_count, 
                'currency_in_title': str(currency_in_title)
                }
            
        except Exception as e:
            logger.fatal("Unable to find current news item")
            
        