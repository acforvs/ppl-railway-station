from abc import ABC, abstractclassmethod
from datetime import datetime, timedelta
from data import schedule
from messages import NEW_CARR, LESS_CARR

class AbstractTrain(ABC):
    '''
    Abstract train class
    '''
    def __init__(self,
                train_id: str = None,
                carriage_num: int = None,
                platform: int = None,
                way: int = None,
                arrival: str = None,
                departure: str = None,
                from_head: bool = None):
        self.train_id = train_id
        self.__carriage_num = carriage_num
        self.platform = platform
        self.way = way
        if not arrival:
            self.arrival = None
        else:
            arrival_input = datetime.strptime(arrival, '%d/%m/%Y %H:%M')
            self.arrival = datetime.combine(arrival_input.date(), 
                                            arrival_input.time())
        if not departure:
            self.departure = None
        else:
            departure_input = datetime.strptime(departure, '%d/%m/%Y %H:%M')
            self.departure = datetime.combine(departure_input.date(), 
                                            departure_input.time())
        self.from_head = from_head

    @property
    def carriage_num(self):
        return self.__carriage_num

    def add_carriages(self, amount, time):
        time = datetime.strptime(time, '%d/%m/%Y %H:%M')
        self.__carriage_num = self.carriage_num + amount
        schedule[time] = NEW_CARR.format(amount, self.train_id, time)

    def remove_carriages(self, amount, time):
        time = datetime.strptime(time, '%d/%m/%Y %H:%M')
        if self.carriage_num >= amount:
            self.__carriage_num = self.carriage_num - amount
        else:
            self.__carriage_num = 0
        schedule[time] = LESS_CARR.format(amount, self.train_id, time)

    def set_arrival(self, arrival):
        try:
            arrival_input = datetime.strptime(arrival, '%d/%m/%Y %H:%M')
            self.arrival = datetime.combine(arrival_input.date(), 
                                            arrival_input.time())
        except:
            raise TypeError('Incorrect arrival format!')

    def set_departure(self, departure):
        try:
            departure_input = datetime.strptime(departure, '%d/%m/%Y %H:%M')
            self.departure = datetime.combine(departure_input.date(), 
                                            departure_input.time())
        except:
            raise TypeError('Incorrect departure format!')

    @abstractclassmethod
    def set_platform(self):
        pass

    @abstractclassmethod
    def set_way(self):
        pass

    @abstractclassmethod
    def delay_arrival(self, delay_time, changes_time):
        pass

    @abstractclassmethod
    def delay_departure(self, delay_time, changes_time):
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
