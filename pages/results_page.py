import logging
import requests
import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

from elements.element import BasePageElement
from locators.results_page_locators import ResultsPageLocators
from pages.base_page import BasePage
from utils.date_parser import DateParser
from utils.currency_parser import CurrencyParser

logger = logging.getLogger(__name__)

class SectionFilterDropDownElement(BasePageElement):
    """
    This class initializes the element for the section dropdown element.
    
    Attributes
    -----------
    locator : By
        locator for the element which will be clicked
    """
    
    def __init__(self, selenium):
        super()
        self.selenium = selenium
        
    locator = ResultsPageLocators.RESULTS_PAGE_SECTION_SELECT_BUTTON_LOCATOR
    
class SectionFilterItemElement(BasePageElement):
    """
    This class find the element for the item in the section dropdown which will be clicked upon.

    Attributes
    ----------
    locator : By
        locator for the element which will be clicked
    
    section : str
        string containing the section in which the user will click on
    """
    
    def __init__(self, selenium, section):
       super()
       self.selenium = selenium
       self.section = section
       self.locator = ResultsPageLocators.RESULTS_PAGE_SECTION_SELECT_ITEM_LOCATOR(self.section)

class SortByOrderDropDownElement(BasePageElement):
    """
    This class initializes the element dropdown which will be clicked for selection of the news' order.
    ie. Newest, Oldest, Relevance
    
    Attributes
    ----------
    locator : By
        locator for the element which will be clicked 
    """
    
    def __init__(self, selenium):
        super()
        self.selenium = selenium
    
    locator = ResultsPageLocators.RESULTS_PAGE_SORT_BY_SELECT_LOCATOR
    
class SortByOrderItemElement(BasePageElement):
    """
    This class initializes the specific item element which will be clicked for the selection of the news' order.
    ie. Newest, Oldest, Relevance
    
    Attributes
    ----------
    locator : By
         locator for the element which will be clicked  
    """
    
    def __init__(self, selenium, order):
        super()
        self.selenium = selenium
        self.order = order
        self.locator = ResultsPageLocators.RESULTS_PAGE_SORT_BY_SELECT_ITEM_LOCATOR(self.order)
        
class HeadingArticleElement(BasePageElement):
    """
    This class initializes the heading for the current item.
    
    Attributes
    ----------
    locator : By
        locator for the element from which the text will be extracted 
    
    index : str
        current index in str format
    """
    
    def __init__(self, selenium, index):
        super()
        self.selenium = selenium
        self.index = index
        self.locator = ResultsPageLocators.RESULT_ITEM_HEADING_LOCATOR(self.index)

class DescriptionArticleElement(BasePageElement):
    """
    This class initializes the descripton for the current item.
    
    Attributes
    -----------
    locator : By
        locator for the element from which the text will be extracted
    
    index : str
        current index in str format
    """
    
    def __init__(self, selenium, index):
        super()
        self.selenium = selenium
        self.index = index
        self.locator = ResultsPageLocators.RESULT_ITEM_DESCRIPTION_LOCATOR(self.index)
        
class DateArticleElement(BasePageElement):
    
    """
    This class initializes the date for the current item.
    
    Attributes
    -----------
    locator : By
        locator for the element from which the text will be extracted
    
    index : str
        current index in str format
    """
    
    def __init__(self, selenium, index):
        super()
        self.selenium = selenium
        self.index = index
        self.locator = ResultsPageLocators.RESULT_ITEM_DATE_LOCATOR(self.index)
        
class ImageArticleElement(BasePageElement):
    """
    This class initializes the image for the current item.
    
    Attributes
    -----------
    locator : By
        locator for the element from which the image data will be extracted
        
    index : str
        current index in str format
    """
    
    def __init__(self, selenium, index):
        super()
        self.selenium = selenium
        self.index = index
        self.locator = ResultsPageLocators.RESULT_ITEM_IMAGE_LOCATOR(self.index)

class TotalResultsElement(BasePageElement):
    """
    This class initializes the total amount of results element.
    
    Attributes
    -----------
    locator : By
        locator for the total amount of results element
    """
    
    def __init__(self, selenium):
       super()
       self.selenium = selenium
    
    locator = ResultsPageLocators.RESULTS_PAGE_TOTAL_ITEMS_LOCATOR
     
class NextStoriesButtonElement(BasePageElement):
    """
    This class initializes the button which will be clicked to load more news.
    
    Attributes
    -----------
    locator : By
        locator for the element which will be clicked
    """
    
    def __init__(self, selenium):
        super()
        self.selenium = selenium
        
    locator = ResultsPageLocators.RESULTS_PAGE_NEXT_STORIES_BUTTON

class ResultsPage(BasePage):
    """
    Class for the results page, the page in which the final results
    from the query appear.
    
    Attributes
    ----------
    selenium: SeleniumLibrary
        instance of SeleniumLibrary which will be used in this page
    """
    
    def __init__(self, selenium, months_index, search_query):
        self.selenium = selenium
        self.months_index = months_index
        self.search_query = search_query

    def _click_section_filter_dropdown(self):
        logger.info("Clicking section filter dropdown.")
        try:
            section_filter_dropdown_element = SectionFilterDropDownElement(self.selenium)
            logger.info("Waiting for SectionFilterDropDownElement to appear...")
            section_filter_dropdown_element.__wait__()
            logger.info("Clicking SectionFilterDropDownElement...")
            section_filter_dropdown_element.__click__()
            logger.info("Clicked SectionFilterDropDownElement successfully! :D")
            return 0
        except Exception as e:
            logger.fatal("Unable to find or click section filter dropdown...")
            return 1
       
    def select_section_filter_from_dropdown(self, section):
        logger.info("Selecting section filter from dropdown.")
        try:
            # Clicking section dropdown
            self._click_section_filter_dropdown()
            
            section_filter_item_element = SectionFilterItemElement(self.selenium, section)
            logger.info("Waiting for SearchBarInputElement to appear...")
            section_filter_item_element.__wait__()
            logger.info("Clicking desired section item in SearchBarInputElement")
            section_filter_item_element.__click__()
            logger.info("Clicked desired section item successfully! :D")     
        except Exception as e:
            logger.fatal("Unable to find or select filter from dropdown")
            return 1

    def select_from_sort_by_order_dropdown(self):
        logger.info("Clicking sort by dropdown.")
        try:
            sort_by_order_dropdown_element = SortByOrderDropDownElement(self.selenium)
            logger.info("Waiting for SortByOrderDropDownElement to appear...")
            sort_by_order_dropdown_element.__wait__()
            logger.info("Clicking SortByOrderDropDownElement...")
            sort_by_order_dropdown_element.__select_by_value__("newest")
            logger.info("Clicked SortByOrderDropDownElement successfully! :D") 
            return 0
        except Exception as e:
            logger.fatal("Unable to find or click sort by dropdown...")
            return 1
 
    def select_sort_by_order_from_dropdown(self, order):
        logger.info("Selecting sort by order from dropdown.")
        try:
            self._click_sort_by_order_dropdown()
            sort_by_order_item_element = SortByOrderItemElement(self.selenium, order)
            logger.info("Waiting for SortByOrderItemElement to appear...")
            sort_by_order_item_element.__wait__()
            logger.info("Clicking desired order item in SortByOrderItemElement")
            logger.info("Selected order successfully! :)")
            return 0
        except Exception as e:
            logger.fatal("Unable to find or select sort by order from dropdown")
            return 1
   
    def _click_next_stories_button(self):
        logger.info("Clicking next stories button.")
        try:
            next_stories_button_element = NextStoriesButtonElement(self.selenium)
            logger.info("Waiting for NextStoriesButtonElement to appear...")
            next_stories_button_element.__wait__()
            logger.info("Clicking NextStoriesButtonElement...")
            next_stories_button_element.__click__()
            logger.info("Clicked NextStoriesButtonElement successfully! :D")
            return 0
        except Exception as e:
            logger.fatal("Unable to find or click next button.")
            return 1
     
    def _download_image(self, image_source, image_filename):
        logger.info("Downloading image...")
        try:
            logger.info("Downloading image from link: ", image_source)
            response = requests.get(image_source)
            
            if response.status_code == 200:
                with open(f"./output/{image_filename}", "wb") as file:
                    file.write(response.content)
                    return
                 
            logger.warning("Something failed while downloading the image...")
            logger.warning("Status Code: ", str(response.status_code))
            return 0 
        except:
            logger.fatal("Failed to download image.")
            return 1
         
    def _iter_through_current_news_article(self, index_current_item, search_query):
        logger.info("Iterating through current news article.")
       
        if index_current_item == 1 or index_current_item == 2:
            current_index_str = str(index_current_item)
        elif index_current_item > 2:
            current_index_str = str(index_current_item - 1)      
            
        try:
            time.sleep(1)
            logger.info("Capturing title from article...")
            title_element = HeadingArticleElement(self.selenium, current_index_str)
            title_element.__wait__()
            
            title = title_element.__get_attribute__("textContent")
            logger.info("Current news article title: ", title)
            
            logger.info("Capturing date from article...") 
            date = DateArticleElement(self.selenium, current_index_str). \
            __get_attribute__("textContent")
           
            #logger.info("Parsing date into proper string") 
            #date = DateParser(date).parse_date_to_proper_string() 
            logger.info("Current news article date: ", str(date))
            
            logger.info("Capturing image from article")
            image = ImageArticleElement(self.selenium, current_index_str)
             
            image_attrs = {}
            image_attrs['src'] = image.__get_attribute__("src")
            
            
            # If current item's index is divisible by 5, move viewport to current image
            if index_current_item % 5 == 0:
                image.__move_to_element__()
                        
            # Initializes variables for image parsing
            image_source = image_attrs['src']
            image_name = title


            # Removes special characters from image alt
            image_name = re.sub('[^A-Za-z0-9 ]+', '', image_name)
            image_filename =  f"{image_name}.jpg"
            
            # Downloads image into output folder 
            self._download_image(image_source, image_filename)
           
            # Gets count of how many times search query appears in article title 
            search_query_count = title.count(search_query)
           
            # Verifies whether there is currency in title 
            currency_in_title = CurrencyParser(title).verifies_title_contains_currency()
                       
            return {
                'title': title,
                'date': date, 
                'filename_image': image_filename, 
                'search_query_count': search_query_count, 
                'currency_in_title': str(currency_in_title)
                }
            
        except Exception as e:
            self._click_next_stories_button()
            logger.fatal("Unable to find current news item")
            
    def _extract_number_of_results_from_total_in_page(self, total_results_string):
        # Captures starting number of articles
        # ie. 1 to 20 -> 1
        pattern_start = r"([0-9]+)+(?= to )"
        
        # Captures ending number of articles
        # ie. 1 to 20 -> 20
        pattern_end = r"(?<= to )([0-9]+)+"
        
        # Searches for starting number pattern in total_results_string
        start_qty_group = re.search(pattern_start, total_results_string).group(0)
        # Casts result as integer
        start_qty_int = int(start_qty_group)
        
        # Searches for ending number pattern in total_resulsts_string
        end_qty_group = re.search(pattern_end, total_results_string).group(0)
        # Casts result as integer
        end_qty_int = int(end_qty_group)
        
        # Returns the total amount of articles in the pattern (+1 is used for including starting number)
        return (end_qty_int - start_qty_int) + 1
        
    def _get_total_items_in_page(self):
        logger.info("Getting total items in page.") 
        try:
            total_results_element = TotalResultsElement(self.selenium)
            logger.info("Waiting for TotalResultsElement to appear...")
            total_results_element.__wait__()
            logger.info("Capturing total results in page...")            
            total_results = total_results_element.__get_total_elements__()
            logger.info("Total number of results in page: ", total_results)
            return total_results
        except Exception as e:
            logger.fatal("Unable to find or capture total amount of results in page.")
            return 1
    
    def _iter_through_current_news_page(self, stop_signal):
        try:
            # Initializes array which will contain the news for the current page
            news_page_array = []
            
            # Initializes final date according to months_index attribute 
            final_date = DateParser.get_final_date(self.months_index)
            
            # Gets total amount of results in page 
            total_results = self._get_total_items_in_page()
           
           # Iterates through total results in page 
            for article_index in range((total_results-10)+1, total_results):
                try:
                    time.sleep(1)
                    # Capture data from current article and stores it in a dictionary
                    current_article = self._iter_through_current_news_article(article_index, self.search_query)
                    # Gets current date 
                    current_date = current_article['date']
                    # Parses current date back into datetime for comparison with final date
                    current_date_parsed_to_datetime = DateParser.parse_string_to_proper_date(current_date)
                
                    # If current date is less than final date, stop capturing articles and return
                    # total no. of results, stop signal and news page array 
                    if current_date_parsed_to_datetime < final_date:
                        stop_signal = True
                        return stop_signal, news_page_array
                    
                    news_page_array.append(current_article)
                except Exception as e:
                    pass
                    
            self._click_next_stories_button()
            
            return stop_signal, news_page_array
        
        except Exception as e:
            return stop_signal, news_page_array
    
    def iter_through_all_news_until_date(self):
       # Initializes array which will contain the news for all pages
       total_news_array = []
       news_array = []
       
       # Initializes stop signal as false 
       stop_signal = False
        
       # While stop signal is not false, process news
       while not stop_signal:
            try:
                stop_signal, news_array = self._iter_through_current_news_page(stop_signal)
            
                # Appends all items in news_array to total_news_array
                [total_news_array.append(x) for x in news_array]    
            except Exception as e:
                [total_news_array.append(x) for x in news_array]
                pass
             
       return total_news_array
        
        
            
        