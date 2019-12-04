from datetime import datetime, timedelta
import random
from train import AbstractTrain
from data import schedule, availability, ways2platforms
from messages import FORMED_WAY, FORMED_PLATFORM, \
    FORMED_ARRIVAL, FORMED_DEPARTURE, \
        FORMED_DELAY_ARRIVAL, FORMED_DELAY_DEPARTURE
from constants import MINUTES_DAY, MINUTES_HOUR

class FormedTrain(AbstractTrain):
    '''
    class for the trains with the route that starts at this platform
    '''
    def __init__(self,
                 train_id: int = None,
                 carriage_num: int = None,
                 platform: int = None,
                 way: int = None,
                 departure: str = None,
                 from_head: bool = None):

        super().__init__(train_id,
                         carriage_num,
                         platform,
                         way,
                         arrival=None,
                         departure=departure,
                         from_head=from_head)


    def set_departure(self, departure_time):
        super().set_departure(departure_time)
        arrival_time = self.departure - timedelta(minutes=20)
        arrival_time = arrival_time.strftime('%d/%m/%Y %H:%M')
        super().set_arrival(arrival_time)

    def arrive(self):
        schedule[self.departure].append(FORMED_ARRIVAL.format(self.train_id))

    def set_platform(self):
        self.platform = random.choice(ways2platforms[self.way])
        delta = timedelta(minutes=30)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FORMED_PLATFORM.format(self.train_id, self.platform))

    def set_way(self):
        delta = timedelta(minutes=30)
        setting_time = self.arrival - delta
        super().set_way(setting_time.strftime('%d/%m/%Y %H:%M'))
        schedule[setting_time].append(FORMED_WAY.format(self.train_id, self.way))

    def delay_arrival(self, delay_time, changes_time):
        super().delay_arrival(delay_time, changes_time, FORMED_DELAY_ARRIVAL)

    def delay_departure(self, delay_time, changes_time):
        super().delay_departure(delay_time, changes_time, FORMED_DELAY_DEPARTURE)

    def depart(self):
        schedule[self.departure].append(FORMED_DEPARTURE.format(self.train_id))

    def process_train(self):
        self.arrive()
        self.set_way()
        self.set_platform()
        self.depart()
        