import logging

from robocorp.tasks import task
from RPA.Robocorp.WorkItems import WorkItems

from lib.extended_selenium import ExtendedSelenium

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.results_page import ResultsPage
from utils.xlsx_serializer import XLSXSerializer

logging.basicConfig(filename='output/RPA_Reuters.log', filemode='a', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S')


@task
def minimal_task():
    search_query = "cookies"
    section = "All"
    months_index = 0
    
    selenium = ExtendedSelenium()
    base_page = BasePage(selenium)
    base_page.access_reuters_page()
    
    home_page = HomePage(selenium)
    home_page.click_search_bar_icon()
    home_page.enter_search_query(search_query)
    home_page.click_search_bar_icon()
    
    results_page = ResultsPage(selenium, months_index, search_query)
    results_page.select_section_filter_from_dropdown(section)
    results_page.select_sort_by_order_from_dropdown("Newest")
    results_array = results_page.iter_through_all_news_until_date()
    
    xlsx_serializer = XLSXSerializer("./output/Reuters.xlsx", "Reuters")
    xlsx_serializer.serialize_news_array_to_excel_file(results_array)
    
    print("brkpt")
