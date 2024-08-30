from robocorp.tasks import task

from lib.extended_selenium import ExtendedSelenium

from pages.base_page import BasePage
from pages.home_page import HomePage

import logging

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
    print("working")
