from datetime import datetime, timedelta
import logging
from data import schedule, availability
from train import AbstractTrain
from messages import FORMED_DELAY_ARRIVAL, FORMED_DELAY_DEPARTURE, \
    FORMED_WAY, FORMED_PLATFORM, \
    FORMED_ARRIVAL, FORMED_DEPARTURE
from constants import MINUTES_DAY, MINUTES_HOUR

class FormedTrain(AbstractTrain):
    '''
    class for the trains with the route that starts at this platform
    '''
    def __init__(self,
                 id: int = None,
                 carriage_num: int = None,
                 platform: int = None,
                 way: int = None,
                 departure: str = None,
                 from_head: bool = None):

        arrival = departure - timedelta(minutes=20)
        super().__init__(id,
                         carriage_num,
                         platform,
                         way,
                         arrival,
                         departure,
                         from_head)

    def L_arrivée_d_un_train(self):
        schedule[self.departure].append(FORMED_ARRIVAL.format(self.id))

    def set_platform(self, platform_num):
        self.platform = platform_num
        delta = timedelta(minutes=30)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FORMED_PLATFORM.format(self.id, self.platform))

    def set_way(self, way_num):
        self.way = way_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FORMED_WAY.format(self.id, self.way))

    def delay_arrival(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time // MINUTES_DAY,
            hours=(
                delay_time -
                delay_time % MINUTES_DAY) // MINUTES_HOUR,
            minutes=delay_time % MINUTES_HOUR)
        self.arrival = self.arrival + delta
        schedule[changes_time].append(FORMED_DELAY_ARRIVAL.format(self.id, delta))

    def delay_departure(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time // MINUTES_DAY,
            hours=(
                delay_time -
                delay_time % MINUTES_DAY) // MINUTES_HOUR,
            minutes=delay_time % MINUTES_HOUR)
        self.departure = self.departure + delta
        schedule[changes_time].append(FORMED_DELAY_DEPARTURE.format(self.id, delta))

    def depart(self):
        schedule[self.departure].append(FORMED_DEPARTURE.format(self.id))
