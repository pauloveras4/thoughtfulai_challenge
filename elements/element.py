from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

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
    

    def __get_total_elements__(self):
        """Gets the total amount of elements"""
        selenium = self.selenium
        
        return len(selenium.driver.find_elements(*self.locator))
    
    def __get_elements__(self):
        """Get elements"""
        selenium = self.selenium
        
        elements = WebDriverWait(selenium.driver, 10).until(
            lambda driver : selenium.driver.find_elements(*self.locator)
        )
        
        return elements
    
    def __get_attribute__(self, attribute):
        """Gets the attribute for the provided element"""
        attribute = self.__get_element__().get_attribute(attribute)
        return attribute
    
    def __wait__(self):
        """Waits 30 seconds for element to appear"""
        selenium = self.selenium
        WebDriverWait(selenium.driver, 60).until(
            EC.presence_of_element_located(
               self.locator 
            )
        )
        
    def __click__(self):
        """Clicks element on screen"""
        self.__get_element__().click()
        
    def __jsclick__(self):
        """Clicks on an element using JS"""
        self.selenium.driver.execute_script("arguments[0].click()", self.__get_element__())
        
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
            
    def __select_by_visible_text__(self, text):
        select = Select(self.__get_element__())
        select.select_by_visible_text(text)
        
    def __select_by_value__(self, value):
        select = Select(self.__get_element__())
        select.select_by_value(value)
