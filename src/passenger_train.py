from datetime import datetime, timedelta
import random
from train import AbstractTrain
from data import schedule, availability, ways2platforms, initialize
from messages import PASSENGER_WAY, PASSENGER_PLATFORM, \
    PASSENGER_ARRIVAL, PASSENGER_DEPARTURE, \
        PASSENGER_DELAY_ARRIVAL, PASSENGER_DELAY_DEPARTURE
from constants import MINUTES_DAY, MINUTES_HOUR

class PassengerTrain(AbstractTrain):
    '''
    passenger train class
    '''
    def __init__(self,
                 train_id: str = None,
                 carriage_num: int = None,
                 platform: int = None,
                 way: int = None,
                 arrival: str = None,
                 departure: str = None,
                 from_head: bool = None):
        super().__init__(train_id,
                         carriage_num,
                         platform,
                         way,
                         arrival,
                         departure,
                         from_head)

    def arrive(self):
        schedule[self.arrival].append(PASSENGER_ARRIVAL.format(self.train_id))

    def set_platform(self):
        self.platform = random.choice(ways2platforms[self.way])
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(PASSENGER_PLATFORM.format(self.train_id, 
                                                            self.platform, 
                                                            self.arrival))
    def set_way(self):
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        super().set_way(setting_time.strftime('%d/%m/%Y %H:%M'))
        schedule[setting_time].append(PASSENGER_WAY.format(self.train_id, self.way))

    def delay_arrival(self, delay_time, changes_time):
        super().delay_arrival(delay_time, changes_time, PASSENGER_DELAY_ARRIVAL)

    def delay_departure(self, delay_time, changes_time):
        super().delay_departure(delay_time, changes_time, PASSENGER_DELAY_DEPARTURE)

    def depart(self):
        schedule[self.departure].append(PASSENGER_DEPARTURE.format(self.train_id))

    def process_train(self):
        self.arrive()
        self.set_way()
        self.set_platform()
        self.depart()
