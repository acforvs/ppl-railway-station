from abc import ABC, abstractclassmethod
from datetime import datetime
import logging
#from data import schedule


logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', 
                    level=logging.DEBUG,
                    datefmt='%d/%m/%Y %H:%M:%S')

schedule = {}

class AbstractTrain(ABC):
    '''
    Abstract train class
    '''
    def _init__(self, 
                id: str=None,
                carriage_num: int=None, 
                platform: int=None, 
                way: int=None, 
                arrival: str=None, 
                departure: str=None, 
                from_head: bool=None):
        self.id = id
        self.carriage_num = carriage_num
        self.platform = platform
        self.way = way
        self.arrival = datetime.strptime(arrival, '%d/%m/%Y %H:%M').time()
        self.departure = datetime.strptime(departure, '%d/%m/%Y %H:%M').time()
        self.from_head = from_head

    @abstractclassmethod
    def set_platform(self, platform):
        pass

    @abstractclassmethod
    def set_way(self, platform):
        pass

    @abstractclassmethod
    def delay_arrival(self, delay_time):
        pass

    @abstractclassmethod
    def delay_departure(self, delay_time):
        pass

class Train(AbstractTrain):
    '''
    passenger train class
    '''
    def __init__(self, 
                id: str=None,
                carriage_num: int=None, 
                platform: int=None, 
                way: int=None, 
                arrival: str=None, 
                departure: str=None, 
                from_head: bool=None):
        super().__init__(id,
                        carriage_num, 
                        platform, 
                        way, 
                        arrival, 
                        departure, 
                        from_head)

    def set_platform(self, platform_num):
        delta = datetime.datetime(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time] = "For train {self.id} the platform {platform_num} was chosen"
    
    def set_way(self, way_num):
        delta = datetime.datetime(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time] = "Fot train {self.id} the platfrom {way_num} was chosen"

    def delay_arrival(self, delay_time):
        delta = datetime.strptime(delay_time, '%d/%m/%Y %H:%M').time()
        self.arrival = self.arrival + delta

    def delay_departure(self, delay_time):
        delta = datetime.strptime(delay_time, '%d/%m/%Y %H:%M').time()
        self.departure = self.departure + delta