from robocorp.tasks import task
from lib.extended_selenium import ExtendedSelenium

@task
def minimal_task():
    selenium = ExtendedSelenium()
    selenium.open_site("https://www.reuters.com")
    selenium.looking_at_element('//*[@id="fusion-app"]/header/div/div/div/div/div[3]/div[1]')
    print("Feito")
