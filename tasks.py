import logging

from robocorp.tasks import task

from lib.extended_selenium import ExtendedSelenium

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.results_page import ResultsPage

logging.basicConfig(filename='RPA_Reuters.log', filemode='a', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S')


@task
def minimal_task():
    selenium = ExtendedSelenium()
    base_page = BasePage(selenium)
    base_page.access_reuters_page()
    
    home_page = HomePage(selenium)
    home_page.click_search_bar_icon()
    home_page.enter_search_text("Israel")
    home_page.click_search_bar_icon()
    
    results_page = ResultsPage(selenium)
    results_page.select_section_filter_from_dropdown("World")
    results_page.select_sort_by_order_from_dropdown("Newest")
    results_page.iter_through_current_news(1)
    print("brkpt")
