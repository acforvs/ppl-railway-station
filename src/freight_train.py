from datetime import datetime, timedelta
import logging
from data import schedule, availability
from train import AbstractTrain
from messages import FREIGHT_ARRIVAL, FREIGHT_DELAY_ARRIVAL, \
    FREIGHT_PLATFORM, FREIGHT_WAY

class FreightTrain(AbstractTrain):
    '''
    freight train
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
        schedule[self.arrival].append(FREIGHT_ARRIVAL.format(self.id))

    def set_platform(self, platform_num):
        self.platform = platform_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FREIGHT_PLATFORM.format(self.id, 
                                                        self.platform, 
                                                        self.arrival))

    def set_way(self, way_num):
        self.way = way_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FREIGHT_WAY.format(self.id, self.way))

    def depart(self):
        raise ValueError('''The freight train should stay here a little longer.
                            There is no depart() func for this train''')

