import logging

from robocorp.tasks import task
from RPA.Robocorp.WorkItems import WorkItems

from lib.custom_selenium import CustomSelenium

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from utils.xlsx_serializer import XLSXSerializer

logging.basicConfig(
   filename='output/RPA_Reuters.log',
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
    search_query = "cookies"
    section = "All"
    months_index = "0"
    months_index = int(months_index)
   
    # Initializing Selenium
    selenium = CustomSelenium()
    selenium.set_webdriver()
    
    # Initializing BasePage
    base_page = BasePage(selenium)
    base_page.access_reuters_page()
    
    home_page = HomePage(base_page.selenium)
    home_page.click_search_bar_icon()
    home_page.enter_search_query(search_query)
    home_page.click_search_bar_icon()
    
    results_page = ResultsPage(home_page.selenium, months_index, search_query)
    results_page.select_section_filter_from_dropdown(section)
    results_page.select_sort_by_order_from_dropdown("Newest")
    results_array = results_page.iter_through_all_news_until_date()
    
    xlsx_serializer = XLSXSerializer("./output/Reuters.xlsx", "Reuters")
    xlsx_serializer.serialize_news_array_to_excel_file(results_array)
    
    print("brkpt")
