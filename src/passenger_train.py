from datetime import datetime, timedelta
import logging
from data import schedule, availability
from train import AbstractTrain
from messages import PASSENGER_DELAY_ARRIVAL, PASSENGER_DELAY_DEPARTURE, \
    PASSENGER_WAY, PASSENGER_PLATFORM, \
    PASSENGER_ARRIVAL, PASSENGER_DEPARTURE
from constants import MINUTES_DAY, MINUTES_HOUR

class PassengerTrain(AbstractTrain):
    '''
    passenger train class
    '''
    def __init__(self,
                 id: str = None,
                 carriage_num: int = None,
                 platform: int = None,
                 way: int = None,
                 arrival: str = None,
                 departure: str = None,
                 from_head: bool = None):
        super().__init__(id,
                         carriage_num,
                         platform,
                         way,
                         arrival,
                         departure,
                         from_head)

    def L_arrivée_d_un_train(self):
        schedule[self.arrival].append(PASSENGER_ARRIVAL.format(self.id))

    def set_platform(self, platform_num):
        self.platform = platform_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(PASSENGER_PLATFORM.format(self.id, 
                                                            self.platform, 
                                                            self.arrival))

    def set_way(self, way_num):
        self.way = way_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(PASSENGER_WAY.format(self.id, self.way))

    def delay_arrival(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time // MINUTES_DAY,
            hours=(
                delay_time -
                delay_time % MINUTES_DAY) // MINUTES_HOUR,
            minutes=delay_time % MINUTES_HOUR)
        self.arrival = self.arrival + delta
        schedule[changes_time].append(PASSENGER_DELAY_ARRIVAL.format(self.id, delta))

    def delay_departure(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time // MINUTES_DAY,
            hours=(
                delay_time -
                delay_time % MINUTES_DAY) // MINUTES_HOUR,
            minutes=delay_time % MINUTES_HOUR)
        self.departure = self.departure + delta
        schedule[changes_time].append(PASSENGER_DELAY_DEPARTURE.format(self.id, delta))

    def depart(self):
        schedule[self.departure].append(PASSENGER_DEPARTURE.format(self.id))


