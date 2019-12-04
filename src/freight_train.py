from datetime import datetime, timedelta
import random
from train import AbstractTrain
from data import schedule, availability, ways2platforms
from messages import FREIGHT_ARRIVAL, FREIGHT_PLATFORM, FREIGHT_WAY

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

    def arrive(self):
        schedule[self.arrival].append(FREIGHT_ARRIVAL.format(self.train_id))

    def set_platform(self):
        self.platform = random.choice(ways2platforms[self.way])
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time].append(FREIGHT_PLATFORM.format(self.train_id, 
                                                        self.platform, 
                                                        self.arrival))
    def set_way(self):
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        super().set_way(setting_time.strftime('%d/%m/%Y %H:%M'))
        schedule[setting_time].append(FREIGHT_WAY.format(self.train_id, self.way))

    def depart(self):
        raise ValueError('''The freight train should stay here a little longer.
                            There is no depart() func for this train''')

    def process_train(self):
        self.arrive()
        self.set_way()
        self.set_platform()
        