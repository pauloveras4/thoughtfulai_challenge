from selenium.webdriver.common.by import By 

class ResultsPageLocators(object):
    """
    A class for storing results page locators. All locators related to
    the home page will be stored in here.
    """

    RESULTS_PAGE_SECTION_SELECT_BUTTON_LOCATOR = (By.XPATH, "//button[@id='sectionfilter']")

    RESULTS_PAGE_SECTION_SELECT_ITEM_LOCATOR = lambda section: (By.XPATH, f"//li[contains(@id, '{section}')]")

    RESULTS_PAGE_SORT_BY_SELECT_BUTTON_LOCATOR = (By.XPATH, "//button[@id='sortby']")
    
    RESULTS_PAGE_SORT_BY_SELECT_ITEM_LOCATOR = lambda order: (By.XPATH, f"//li[contains(@data-key, '{order}')]")
    
    RESULTS_PAGE_SEARCH_RESULT_ITEM_LOCATOR = lambda index: (By.XPATH, f"(//li[contains(@class, 'search-results__item')])[{index}]")

    RESULTS_PAGE_TOTAL_ITEMS_LOCATOR = (By.XPATH, f"//span[contains(@class, 'search-results__text')]") 

    RESULTS_PAGE_NEXT_STORIES_BUTTON = (By.XPATH, f"//button[contains(@aria-label, 'Next stories')]")
                                        
    RESULT_ITEM_HEADING_LOCATOR = lambda index: (By.XPATH, f"(//li[contains(@class, 'search-results__item')]//span[@data-testid='Heading'])[{index}]")
  
    RESULT_ITEM_DATE_LOCATOR = lambda index: (By.XPATH, f"(//li[contains(@class, 'search-results__item')]//time[@data-testid='Text'])[{index}]")
    
    RESULT_ITEM_IMAGE_LOCATOR = lambda index: (By.XPATH, f"(//li[contains(@class, 'search-results__item')]//img)[{index}]")
    

