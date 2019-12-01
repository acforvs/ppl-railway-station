from datetime import datetime, timedelta
from collections import namedtuple

ways2platforms = {}
schedule = {}
availability = {}
trains = {}
events = []

sign = lambda a: (a>0) - (a<0)

def create_dict(date):
    date_input = datetime.strptime(date, '%d/%m/%Y').date() - timedelta(days=1)
    time_input = datetime.strptime('23:30', '%H:%M').time()
    time_start = datetime.combine(date_input, time_input)
    for delta in range(0, 1471):
        final = time_start + \
            timedelta(days=delta // 1440, 
                    hours=delta // 60, 
                    minutes=delta % 60)
        availability[final] = set()
        schedule[final] = []
