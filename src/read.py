from parser import Parser
from itertools import repeat
from data import ways2platforms, train, trains
from collections import namedtuple

def read():
    pathGetter = Parser()
    path = pathGetter.process_arguments()

    if not path: 
        return None

    with open(path, 'r'):
        try:
            date = str(input())
            trains_cnt, events_cnt, conn_cnt = map(int, input().split())
            platforms_amount, ways_amount = map(int, input().split())
            event_descr = namedtuple('event', 'description')
            events = []

            for _ in repeat(None, conn_cnt):
                platform, way = map(int, input().split())
                if way in ways2platforms:
                    ways2platforms[way].append(platform)
                else:
                    ways2platforms[way] = []

            for _ in repeat(None, trains_cnt):
                id, carriages = map(int, input().split())
                route, train_type = map(str, input().split())
                info = train(carriages, route, train_type)
                trains[id] = info

            for _ in repeat(None, events_cnt):
                descr = str(input())
                event = event_descr(descr)
                events.append(event)

            data = namedtuple('data', ['date', 'platforms', 'ways', 'events'])
            result = data(date, platforms_amount, ways_amount, events)

            return result

        except:
            raise OSError('No such file')

        







