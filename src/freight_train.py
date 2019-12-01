from datetime import datetime, timedelta
import logging
import random
from data import schedule, availability, ways2platforms
from train import AbstractTrain
from messages import FREIGHT_ARRIVAL, FREIGHT_DELAY_ARRIVAL, \
    FREIGHT_PLATFORM, FREIGHT_WAY

class FreightTrain(AbstractTrain):
    '''
    freight train
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

    def L_arrivée_d_un_train(self):
        schedule[self.arrival].append(FREIGHT_ARRIVAL.format(self.train_id))

    def set_platform(self):
        self.platform = random.choice(ways2platforms[self.way])
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FREIGHT_PLATFORM.format(self.train_id, 
                                                        self.platform, 
                                                        self.arrival))

    def delay_arrival(self, delay_time, changes_time):
        pass

    def delay_departure(self, delay_time, changes_time):
        pass

    def set_way(self):
        delta = timedelta(minutes=10)
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
        schedule[setting_time].append(FREIGHT_WAY.format(self.train_id, self.way))

    def depart(self):
        raise ValueError('''The freight train should stay here a little longer.
                            There is no depart() func for this train''')

    def process_train(self):
        self.L_arrivée_d_un_train()
        self.set_way()
        self.set_platform()
        self.depart()
        