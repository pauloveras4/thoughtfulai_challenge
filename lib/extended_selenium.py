from RPA.Browser.Selenium import Selenium
from webdrivermanager import ChromeDriverManager
from SeleniumLibrary.base import keyword
from selenium import webdriver

class ExtendedSelenium(Selenium):

    def __init__(self, *args, **kwargs):
        Selenium.__init__(self, *args, **kwargs)
        cdm = ChromeDriverManager(link_path="AUTO")
        cdm.download_and_install()
    
    def set_firefox_options(self):
        firefox_options = {
            "arguments": [
                "--headless"  # Enable headless mode
            ]
        }
        return firefox_options
    
    @keyword
    def looking_at_element(self, locator):
        element = self.get_webelement(locator)
        self.logger.warn(dir(element))

    @keyword
    def open_site(self, url, **kwargs):
        desired_capabilities = {
            "goog:loggingPrefs" : { 'browser':'ALL',  'driver': 'ALL', 'performance': 'ALL' }
        }
        options = self.set_firefox_options()
        self.open_browser(
            url=url,
            desired_capabilities=desired_capabilities,
            options=options,
            **kwargs
        )

    @keyword
    def print_webdriver_log(self, logtype):
        print(f"\n{logtype.capitalize()} Log")
        return self.driver.get_log(logtype)
        