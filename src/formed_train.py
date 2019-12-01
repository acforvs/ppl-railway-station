from datetime import datetime, timedelta
import logging
import random
from data import schedule, availability, ways2platforms
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
                 train_id: int = None,
                 carriage_num: int = None,
                 platform: int = None,
                 way: int = None,
                 departure: str = None,
                 from_head: bool = None):

        arrival = departure - timedelta(minutes=20)
        super().__init__(train_id,
                         carriage_num,
                         platform,
                         way,
                         arrival,
                         departure,
                         from_head)

    def L_arrivée_d_un_train(self):
        schedule[self.departure].append(FORMED_ARRIVAL.format(self.train_id))

    def set_platform(self):
        self.platform = random.choice(ways2platforms[self.way])
        delta = timedelta(minutes=30)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FORMED_PLATFORM.format(self.train_id, self.platform))

    def set_way(self):
        delta = timedelta(minutes=30)
        setting_time = self.arrival - delta
        self.way = random.choice(list(availability[setting_time]))
        for delta in range(0, (self.departure - self.arrival).seconds // 60):
            final = setting_time + \
                timedelta(days=0, 
                        hours=delta // 60, 
                        minutes=delta % 60)
            try:
                availability[final].remove(self.way)
            except:
                pass
        schedule[setting_time].append(FORMED_WAY.format(self.train_id, self.way))

    def delay_arrival(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M')
        delta = timedelta(
            days=delay_time // MINUTES_DAY,
            hours=(
                delay_time -
                delay_time % MINUTES_DAY) // MINUTES_HOUR,
            minutes=delay_time % MINUTES_HOUR)
        self.arrival = self.arrival + delta
        schedule[changes_time].append(FORMED_DELAY_ARRIVAL.format(self.train_id, delta))

    def delay_departure(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M')
        delta = timedelta(
            days=delay_time // MINUTES_DAY,
            hours=(
                delay_time -
                delay_time % MINUTES_DAY) // MINUTES_HOUR,
            minutes=delay_time % MINUTES_HOUR)
        for delta in range(0, delay_time):
            final = self.departure + \
                timedelta(days=0, 
                        hours=delta // 60, 
                        minutes=delta % 60)
            try:
                availability[final].remove(self.way)
            except:
                pass
        self.departure = self.departure + delta
        schedule[changes_time].append(FORMED_DELAY_DEPARTURE.format(self.train_id, delta))

    def depart(self):
        schedule[self.departure].append(FORMED_DEPARTURE.format(self.train_id))

    def process_train(self):
        self.L_arrivée_d_un_train()
        self.set_way()
        self.set_platform()
        self.depart()
        