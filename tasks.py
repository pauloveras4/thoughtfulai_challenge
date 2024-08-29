from robocorp.tasks import task

from lib.extended_selenium import ExtendedSelenium

from pages.base_page import BasePage

import logging

logging.basicConfig(filename='RPA_Reuters.log', filemode='a', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S')


@task
def minimal_task():
    selenium = ExtendedSelenium()
    base_page = BasePage(selenium)
    base_page.access_reuters_page()
