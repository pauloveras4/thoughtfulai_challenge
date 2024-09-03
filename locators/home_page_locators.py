from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """
    A class for storing home page locators. All locators related to
    the home page will be stored in here.
    """

    HOME_PAGE_ACCEPT_ALL_COOKIES_BUTTON = (By.XPATH,"(//button[contains(@data-testid, 'Accept')])[1]" )
    
    HOME_PAGE_SEARCH_BAR_ICON_LOCATOR = (By.XPATH, "//button[contains(@aria-controls, 'search-input')]")

    HOME_PAGE_SEARCH_BAR_INPUT_LOCATOR = (By.XPATH, "//input[contains(@data-testid, 'search-input')]")
    