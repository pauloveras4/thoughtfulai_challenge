class ResultsPageLocators(object):
    """
    A class for storing results page locators. All locators related to
    the home page will be stored in here.
    """

    RESULTS_PAGE_SECTION_SELECT_BUTTON_LOCATOR = "//button[@id='sectionfilter']"

    RESULTS_PAGE_SECTION_SELECT_ITEM_LOCATOR = lambda section: f"//li[contains(@id, '{section}')]"

    RESULTS_PAGE_SORT_BY_SELECT_BUTTON_LOCATOR = "//button[@id='sortby']"
    
    RESULTS_PAGE_SORT_BY_SELECT_ITEM_LOCATOR = lambda order: f"//li[contains(@data-key, '{order}')]"
    
    RESULTS_PAGE_SEARCH_RESULT_ITEM_LOCATOR = lambda index: f"(//li[contains(@class, 'search-results__item')])[{index}]"
    
    RESULT_ITEM_HEADING_LOCATOR = lambda index: f"(//li[contains(@class, 'search-results__item')]//span[@data-testid='Heading'])[{index}]"
  
    RESULT_ITEM_DATE_LOCATOR = lambda index: f"(//li[contains(@class, 'search-results__item')]//time[@data-testid='Text'])[{index}]"