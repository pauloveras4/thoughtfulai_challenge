from selenium.webdriver.common.by import By 

class ResultsPageLocators(object):
    """
    A class for storing results page locators. All locators related to
    the home page will be stored in here.
    """

    RESULTS_PAGE_SECTION_SELECT_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@data-testid, 'search-multiselect-button')]/label[contains(., 'Section')]")

    RESULTS_PAGE_SECTION_SELECT_ITEM_LOCATOR = lambda section: (By.XPATH, f"//li/label[contains(., '{section}')]")

    RESULTS_PAGE_SORT_BY_SELECT_LOCATOR = (By.XPATH, "//select")
    
    RESULTS_PAGE_SORT_BY_SELECT_ITEM_LOCATOR = lambda order: (By.XPATH, f"//li[contains(@data-key, {order})]")
    
    RESULTS_PAGE_SEARCH_RESULT_ITEM_LOCATOR = lambda index: (By.XPATH, f"(//li[contains(@class, 'search-results__item')])[{index}]")

    RESULTS_PAGE_TOTAL_ITEMS_LOCATOR = (By.XPATH, f"//li[contains(@data-testid, 'search-bodega-result')]") 

    RESULTS_PAGE_NEXT_STORIES_BUTTON = (By.XPATH, f"//button[contains(@data-testid, 'search-show-more-button')]")
    
    RESULTS_TOTAL_ITEM_ELEMENTS = (By.XPATH, f"//ol[contains(@data-test-id, 'search-results)]//span[contains(2data-testid, 'todays-date')]")
                                        
    RESULT_ITEM_HEADING_LOCATOR = lambda index: (By.XPATH, f"(//ol[contains(@data-testid, 'search-results')]/li//h4)[{index}]")
    
    RESULT_ITEM_DESCRIPTION_LOCATOR = lambda index: (By.XPATH, f"(//ol[contains(@data-testid, 'search-results')]/li[{index}]/div/div/div/a/p)[1]")
  
    RESULT_ITEM_DATE_LOCATOR = lambda index: (By.XPATH, f"(//ol[contains(@data-testid, 'search-results')]/li//span[contains(@data-testid, 'todays-date')])[{index}]")
    
    RESULT_ITEM_IMAGE_LOCATOR = lambda index: (By.XPATH, f"(//ol[contains(@data-testid, 'search-results')]/li//img)[{index}]")
    

