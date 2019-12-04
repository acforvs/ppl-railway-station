from datetime import datetime, timedelta
from parser import Parser
from itertools import repeat
from data import ways2platforms, trains, events, availability, initialize
from collections import namedtuple
from passenger_train import PassengerTrain
from freight_train import FreightTrain
from formed_train import FormedTrain
from usage import ARGUMENTS
from constants import MINUTES_DAY, MINUTES_HOUR

sign = lambda a: (a>0) - (a<0)

def read():
    # getting the file path
    pathGetter = Parser()
    path = pathGetter.process_arguments()

    if not path: 
        print(ARGUMENTS)
        raise Exception('No file path')

    with open(path, 'r') as input_schedule:
        try:
            # reading from file
            date = str(input_schedule.readline().split()[0])
            initialize(date)
            # amount of trains, events and connections
            second_line = input_schedule.readline().split()
            trains_cnt, events_cnt, conn_cnt = int(second_line[0]), int(second_line[1]), int(second_line[2])
            
            # [amount of platforms] [amount of ways]
            third_line = input_schedule.readline().split()
            platforms_amount, ways_amount = int(third_line[0]), int(third_line[1])

            event_descr = namedtuple('event', ['id', 'description'])

            date_input = datetime.strptime(date, '%d/%m/%Y').date()
            time_input = datetime.strptime('23:30', '%H:%M').time()
            time_start = datetime.combine(date_input, time_input) - timedelta(days=1)

            for _ in repeat(None, conn_cnt):
                # [platform number] [way number]
                k_lines = input_schedule.readline().split()
                platform, way = int(k_lines[0]), int(k_lines[1])

                if (platform > platforms_amount or way > ways_amount):
                    raise ValueError('Incorrect platform or way number')

                availability[time_start].add(way)

                if way in ways2platforms:
                    ways2platforms[way].append(platform)
                else:
                    ways2platforms[way] = []
                    ways2platforms[way].append(platform)

            for _ in repeat(None, trains_cnt):
                # [train number] [amount of carriages] [train type]
                n_lines = input_schedule.readline().split()
                train_id, carriages, train_type = int(n_lines[0]), int(n_lines[1]), str(n_lines[2])

                if (train_type == 'P'):
                    trains[train_id] = PassengerTrain(train_id=train_id, carriage_num=carriages)
                if (train_type == 'F'):
                    trains[train_id] = FreightTrain(train_id=train_id, carriage_num=carriages)
                if (train_type == 'E'):
                    trains[train_id] = FormedTrain(train_id=train_id, carriage_num=carriages)

            for _ in repeat(None, events_cnt):
                # [train number] [event]
                info = input_schedule.readline().split()
                train_num = int(info[0])
                descr = info[1:]
                event = event_descr(train_num, descr)
                events.append(event)

            for delta in range(0, 1471):
                final = time_start + \
                    timedelta(days=delta // MINUTES_DAY, 
                    hours=(delta % MINUTES_DAY) // MINUTES_HOUR, 
                    minutes=delta % MINUTES_HOUR)
                availability[final] = availability[time_start]

        except:
            raise OSError('No such file')
        