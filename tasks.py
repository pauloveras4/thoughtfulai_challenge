import logging
import time

from robocorp.tasks import task
from RPA.Robocorp.WorkItems import WorkItems

from lib.custom_selenium import CustomSelenium

from selenium_stealth import stealth

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from utils.xlsx_serializer import XLSXSerializer

logging.basicConfig(
   filename='output/RPA_NYTimes.log',
   filemode='a',
   level=logging.INFO,
   format='%(asctime)s %(message)s',
   datefmt='%d/%m/%Y %I:%M:%S'
   )


@task
def minimal_task():
    """
    items = WorkItems()
    variables = items.get_work_item_variables()
    search_query = variables['search_query']
    section = variables['section']
    months_index = variables['months_index']
    """
    search_query = "cookie"
    section = "Any"
    months_index = "0"
    months_index = int(months_index)
   
    # Initializing Selenium
    selenium = CustomSelenium()
    selenium.set_webdriver()
   
    # Selenium on Stealth Mode!!! 
    stealth(selenium.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True
            )


    # Initializing BasePage
    base_page = BasePage(selenium)
    base_page.access_ny_times_page()
   
    time.sleep(5)
    
    home_page = HomePage(selenium)
    home_page.click_accept_all_cookies_button()
    home_page.click_search_bar_icon()
    home_page.enter_search_query(search_query)
    
    results_page = ResultsPage(selenium, months_index, search_query)
    results_page.select_section_filter_from_dropdown(section)
    results_page.select_from_sort_by_order_dropdown()
    time.sleep(2)
    results_array = results_page.iter_through_all_news_until_date()
    
    xlsx_serializer = XLSXSerializer("./output/NYTimes.xlsx", "NYTimes")
    xlsx_serializer.serialize_news_array_to_excel_file(results_array)
    
    print("brkpt")
