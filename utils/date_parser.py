from datetime import date, datetime, timedelta, timezone
from dateutil.relativedelta import relativedelta

class DateParser(object):
    
    def __init__(self, date):
        self.date = date
        
    def parse_date_to_proper_string(self):
        
        if "a min ago" in self.date:
            amt_minutes = -1
            
            delta = timedelta(minutes=amt_minutes)
            
            # Adjusting for Chicago timezone
            gmt_minus_5 = timezone(timedelta(hours=-5))
            current_time_gmt_minus_5 = datetime.now(gmt_minus_5)
            
            news_date = current_time_gmt_minus_5 - delta
            return datetime.strftime(news_date, "%Y-%m-%d %H>%M")
        
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
            try:
                date_today = date.today().strftime("%Y-%m-%d")
                hour_and_minute_without_timezone = self.date[:-6]
                
                datetime_without_timezone = f"{date_today} {hour_and_minute_without_timezone}"                                
                parsed_datetime = datetime.strptime(datetime_without_timezone, "%Y-%m-%d %I:%M %p")
                
                timezone_offset = self.date[-6:]
                timezone_sign = 1 if timezone_offset[3] == '+' else -1 
                timezone_hours = int(timezone_offset[5:])
                
                news_datetime = parsed_datetime - timedelta(hours=timezone_sign * timezone_hours)
                
                # Adjusting for Chicago timezone
                gmt_minus_5 = timezone(timedelta(hours=5))
                
                news_datetime = news_datetime - gmt_minus_5.utcoffset(news_datetime) 
                return datetime.strftime(news_datetime, "%Y-%m-%d %H:%M")
            except Exception as e:
                return 1
        news_date = datetime.strptime(self.date, "%B %d, %Y")
        return datetime.strftime(news_date, "%Y-%m-%d %H:%M")
    
    @staticmethod
    def parse_string_to_proper_date(date):
        return datetime.strptime(date, "%Y-%m-%d %H:%M")
   
    @staticmethod
    def get_final_date(months_index):
        if months_index < 0:
            return 1
        if months_index == 0:
           current_month_datetime = datetime.now() - relativedelta(months=1)
           return current_month_datetime

        previous_months_datetime = datetime.now() - relativedelta(months=months_index)
        return previous_months_datetime

             
   
