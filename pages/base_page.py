import time
import os
import glob
import shutil
import logging

logger = logging.getLogger(__name__)


class BasePage(object):
    """
    Base class to initialize the base page that will store relevant
    stuff for all pages.
    """

    def __init__(self, selenium):
        self.selenium = selenium
    
    def access_reuters_page(self):
        """
        Access Reuters page @ www.reuters.com.    
        """
        logger.info("Accessing Reuters page.")
        try:
            self.selenium.open_site("https://www.reuters.com")
            return 0
        except:
            logger.error("An error occurred while trying to access Reuters page.")
            return 1