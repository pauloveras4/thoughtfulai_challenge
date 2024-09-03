import logging


from locators.base_page_locators import BasePageLocators

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
    
    def access_ny_times_page(self):
        """
        Access New York Times page @ www.nytimes.com.
        
        Returns:
        -------
            0 (int): if everything went smooth, it will return 0! :)
            1 (int): whoops, there was a problem accessing the site...
            2 (int): there was a problem locating the header element
        """
        logger.info("Accessing New York Times page.")
        try:
            self.selenium.open_url("https://www.nytimes.com")
            logger.info("Checking news header exists.")
        except Exception as e:
            logger.error("An error occurred while trying to access New York Times page.")
            return 1