from abc import ABC, abstractclassmethod
from datetime import datetime, timedelta

class AbstractTrain(ABC):
    '''
    Abstract train class
    '''
    def _init__(self,
                id: str = None,
                carriage_num: int = None,
                platform: int = None,
                way: int = None,
                arrival: str = None,
                departure: str = None,
                from_head: bool = None):
        self.id = id
        self.__carriage_num = carriage_num
        self.platform = platform
        self.way = way
        arrival_input = datetime.strptime(arrival, '%d/%m/%Y %H:%M')
        self.arrival = datetime.combine(arrival_input.date(), 
                                        arrival_input.time())
        departure_input = datetime.strptime(departure, '%d/%m/%Y %H:%M')
        self.departure = datetime.combine(departure_input.date(), 
                                        departure_input.time())
        self.from_head = from_head

    @property
    def carriage_num(self):
        return self.__carriage_num

    @carriage_num.setter
    def add_carriages(self, amount):
        self.__carriage_num = self.carriage_num + amount

    @carriage_num.setter
    def remove_carriages(self, amount):
        if self.__carriage_num >= amount:
            self.__carriage_num = self.carriage_num - amount
        else:
            self.__carriage_num = 0

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

    # okay I can change the name but you have to check this out
    # https://en.wikipedia.org/wiki/L%27Arrivée_d%27un_train_en_gare_de_La_Ciotat
    @abstractclassmethod
    def L_arrivée_d_un_train(self):
        pass

    @abstractclassmethod
    def depart(self):
        pass

    @abstractclassmethod
    def process_train(self):
        pass

