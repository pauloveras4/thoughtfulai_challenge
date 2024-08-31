import re

class CurrencyParser(object):
    
    def __init__(self, title):
        self.title = title
        
    def verifies_title_contains_currency(self):
        
        array_verify_currency = [
            self._verifies_currency_up_to_hundreds(self.title),
            self._verifies_currency_up_to_thousands(self.title),
            self.verifies_currency_up_to_dozens(self.title),
            self.verifies_currency_up_to_dozens_iso4217(self.title)
        ]
        
        is_there_currency_in_title = any(array_verify_currency)    
        return is_there_currency_in_title
        
    def _verifies_currency_up_to_hundreds(self):
        pattern = r"(\$[0-9]+(\.[0-9]+)?)"
        match = re.match(pattern, self.title)
        
        if match is not None:
            return True

        return False

    def _verifies_currency_up_to_thousands(self):
        pattern = r"(\$[0-9]+\,[0-9]+.[0-9]+)+"
        match = re.match(pattern, self.title)
        
        if match is not None:
            return True

        return False
    
    def _verifies_currency_up_to_dozens(self):
        pattern = r"([0-9]+)(?= dollars)"
        match = re.match(pattern, self.title)
        
        if match is not None:
            return True
        
        return False
   
    def _verifies_currency_up_to_dozens_iso_4217(self):
        pattern = r"([0-9]+)(?= USD)"
        match = re.match(pattern, self.title)
        
        if match is not None:
            return True
        
        return False 
    
    