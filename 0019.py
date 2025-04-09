#How many Sundays fell on the first of the month from 1st Jan 1901 - 31 Dec 2000
#This is a hard problem if we don't use libraries and instead do it manually 
#by iterating through the the days and then dividing by 7 to see if it is a Sunday
#and then checking if it was the first of the month for that year 
#Instead we are going to use datetime library to make it easy

import datetime as dt
from dateutil.relativedelta import relativedelta
def number_of_sundays():
    count = 0
    start_date = dt.date(1901, 1, 1)
    end_date = dt.date(2000, 12, 31)
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 6: #6 equals sunday
            count += 1
        current_date += relativedelta(months=1)   
    return count

print(number_of_sundays())

