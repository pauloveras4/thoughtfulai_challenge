from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """
    A class for storing home page locators. All locators related to
    the home page will be stored in here.
    """

    HOME_PAGE_SEARCH_BAR_ICON_LOCATOR = (By.XPATH, "//div[contains(@class, 'search-bar')]")

    HOME_PAGE_SEARCH_BAR_INPUT_LOCATOR = (By.XPATH, "//input[@data-testid='FormField:input']")
    