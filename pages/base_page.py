from locators.base_page_locators import BasePageLocators
import logging

logger = logging.getLogger(__name__)


class BasePage(object):
    """
    Base class to initialize the base page that will store relevant
    stuff for all pages.
    
    Attributes
    ----------
    selenium : SeleniumLibrary
        instance of SeleniumLibrary which will be used across all pages
    """

    def __init__(self, selenium):
        self.selenium = selenium
    
    def access_reuters_page(self):
        """
        Access Reuters page @ www.reuters.com.
        
        Returns:
        -------
            0 (int): if everything went smooth, it will return 0! :)
            1 (int): whoops, there was a problem accessing the site...
            2 (int): there was a problem locating the header element
        """
        logger.info("Accessing Reuters page.")
        try:
            self.selenium.open_site("https://www.reuters.com")
            logger.info("Checking news header exists.")
            element_exists = self.selenium.is_element_enabled(
                            BasePageLocators.BASE_PAGE_SITE_HEADER_LOCATOR)
            if element_exists:
                return 0
            logger.warning("Header not found!")
            return 2
        except:
            logger.error("An error occurred while trying to access Reuters page.")
            return 1