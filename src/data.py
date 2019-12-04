from datetime import datetime, timedelta
from collections import namedtuple
from constants import MINUTES_DAY, MINUTES_HOUR

ways2platforms = {}
schedule = {}
availability = {}
trains = {}
events = []

sign = lambda a: (a>0) - (a<0)

def initialize(date):  
        # getting the date of the schedule
        date_input = datetime.strptime(date, '%d/%m/%Y').date() - timedelta(days=1)
        time_input = datetime.strptime('23:30', '%H:%M').time()
        time_start = datetime.combine(date_input, time_input)
        for delta in range(0, 1471):
                # creating the set for available ways at [final] time 
                final = time_start + \
                        timedelta(days=delta // MINUTES_DAY, 
                        hours=(delta % MINUTES_DAY) // MINUTES_HOUR, 
                        minutes=delta % MINUTES_HOUR)
                availability[final] = set()
                schedule[final] = []
