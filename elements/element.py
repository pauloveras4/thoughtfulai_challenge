from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    """
    Base page class that is initialized on every page object class.
    """        
    def __set__(self, value):
        """Sets the text to the value supplied"""
        
        selenium = self.selenium
        WebDriverWait(selenium.driver, 100).until(
            lambda driver: selenium.driver.find_element(*self.locator)
        )
        
        selenium.driver.find_element(*self.locator).clear()
        selenium.driver.find_element(*self.locator).send_keys(value)
        
    def __get__(self):
        """Gets the text of the specified object"""
        selenium = self.selenium
        
        WebDriverWait(selenium.driver, 100).until(
            lambda driver: selenium.driver.find_element(*self.locator)
        )
        
        element = selenium.driver.find_element(self.locator)
        return element.get_attribute("textContent")
    
    def __get_element__(self):
        """Gets the element for the object"""
        selenium = self.selenium
        
        element = WebDriverWait(selenium.driver, 10).until(
            lambda driver : selenium.driver.find_element(*self.locator)
        )
        return element
    
    def __get_attribute__(self, attribute):
        """Gets the attribute for the provided element"""
        attribute = self.__get_element__().get_attribute(attribute)
        return attribute
    
    def __wait__(self):
        """Waits 15 seconds for element to appear"""
        selenium = self.selenium
        WebDriverWait(selenium.driver, 15).until(
            EC.presence_of_element_located(
               self.locator 
            )
        )
        
    def __click__(self):
        """Clicks element on screen"""
        self.__get_element__().click()
        
    def __send_key__(self, key):
        """Sends input from the keyboard to the element"""
        selenium = self.selenium
        self.__get_element__().send_keys(*key)
        
    def __move_to_element__(self):
        self.selenium.driver.execute_script("arguments[0].scrollIntoView(true);", self.__get_element__())
        self.action_chains = ActionChains(self.selenium.driver)
        self.action_chains \
            .move_to_element(self.__get_element__()) \
            .perform()