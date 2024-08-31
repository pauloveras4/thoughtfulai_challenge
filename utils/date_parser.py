from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta

class DateParser(object):
    
    def __init__(self, date):
        self.date = date
        
    def parse_date_to_proper_string(self):
        if "min ago" in self.date:
            amt_minutes = int(self.date[:-8])
            amt_minutes *= -1
            
            delta = timedelta(minutes=amt_minutes)
            
            # Adjusting for Chicago timezone
            gmt_minus_5 = timezone(timedelta(hours=-5))
            current_time_gmt_minus_5 = datetime.now(gmt_minus_5)
            
            news_date = current_time_gmt_minus_5 - delta
            return datetime.strftime(news_date, "%Y-%m-%d %H:%M")
        
        if "an hour ago" in self.date:
            delta = timedelta(hours=-1)
            
            # Adjusting for Chicago timezone
            gmt_minus_5 = timezone(timedelta(hours=-5))
            current_time_gmt_minus_5 = datetime.now(gmt_minus_5)
            
            news_date = current_time_gmt_minus_5 - delta
            return datetime.strftime(news_date, "%Y-%m-%d %H:%M") 
        
        if ("PM" in self.date) or ("AM" in self.date):
            date_without_timezone = self.date[:-6]
            parsed_date = datetime.strptime(date_without_timezone, "%I:%M %p")
            
            timezone_offset = self.date[-6:]
            timezone_sign = 1 if timezone_offset[3] == '+' else -1 
            timezone_hours = int(timezone_offset[4:])
            
            news_date = parsed_date - timedelta(hours=timezone_sign * timezone_hours) 
            return datetime.strftime(news_date, "%Y-%m-%d %H:%M")

        news_date = datetime.strptime(self.date, "%B %d, %Y")
        return datetime.strftime(news_date, "%Y-%m-%d %H:%M")
    
    def parse_string_to_proper_date(self, date):
        return datetime.strptime(date, "%Y-%m-%d %H:%M")
            
    