from datetime import datetime, timedelta

schedule = {}
availability = {}

def create_dict(date):
    date_input = datetime.strptime(date, '%d/%m/%Y').date()
    time_input = datetime.strptime('00:00', '%H:%M').time()
    time_start = datetime.combine(date_input, time_input)
    for delta in range(-30, 1441):
        final = time_start + \
            timedelta(days=0, 
                    hours=delta // 60, 
                    minutes=delta % 60)
        availability[final] = {}
        schedule[final] = []
