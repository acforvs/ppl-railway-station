from abc import ABC, abstractclassmethod
from datetime import datetime, timedelta
import random
from data import schedule, availability
from messages import NEW_CARR, LESS_CARR
from constants import MINUTES_DAY, MINUTES_HOUR

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
        self.__train_id = train_id
        self.__carriage_num = carriage_num
        self.platform = platform
        self.way = way
        if not arrival:
            self.__arrival = None
        else:
            self.__arrival = datetime.strptime(arrival, '%d/%m/%Y %H:%M')
        if not departure:
            self.__departure = None
        else:
            self.__departure = datetime.strptime(departure, '%d/%m/%Y %H:%M')
        self.from_head = from_head
    
    # getters section
    @property
    def train_id(self):
        return self.__train_id

    @property
    def arrival(self):
        return self.__arrival

    @property
    def departure(self):
        return self.__departure
        
    @property
    def carriage_num(self):
        return self.__carriage_num

    def add_carriages(self, amount, time):
        ''' 
        Adding [amount] of carriages in time
        '''
        time = datetime.strptime(time, '%d/%m/%Y %H:%M')
        self.__carriage_num = self.carriage_num + amount
        schedule[time].append(NEW_CARR.format(amount, self.train_id, time))

    def remove_carriages(self, amount, time):
        ''' 
        Removing [amount] of carriages in time
        '''
        time = datetime.strptime(time, '%d/%m/%Y %H:%M')
        if self.carriage_num >= amount:
            self.__carriage_num = self.carriage_num - amount
        else:
            self.__carriage_num = 0
        schedule[time].append(LESS_CARR.format(amount, self.train_id, time))

    def set_arrival(self, arrival_time):
        ''' 
        Setting the arrival time as [arrival]
        '''
        try:
            arrival_input = datetime.strptime(arrival_time, '%d/%m/%Y %H:%M')
            self.__arrival = arrival_input
        except:
            raise TypeError('Incorrect arrival format!')

    def set_departure(self, departure_time):
        ''' 
        Setting the departure time as [departure]
        '''
        try:
            self.__departure = datetime.strptime(departure_time, '%d/%m/%Y %H:%M')
        except:
            raise TypeError('Incorrect departure format!')

    @abstractclassmethod
    def set_platform(self, setting_time):
        '''
        Setting the platform randomly at [setting_time]
        '''
        pass

    def set_way(self, setting_time):
        '''
        Setting the way randomly at [setting_time]
        '''
        setting_time = datetime.strptime(setting_time, '%d/%m/%Y %H:%M')
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

    def delay_arrival(self, delay_time, changes_time, train_mess):
        '''
        Delaying the arrival for [delay_time]. Action happens at [changes_time]
        '''
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M')
        delta = timedelta(
            days=delay_time // MINUTES_DAY,
            hours=(
                delay_time -
                delay_time % MINUTES_DAY) // MINUTES_HOUR,
            minutes=delay_time % MINUTES_HOUR)
        self.__arrival = self.arrival + delta
        schedule[changes_time].append(train_mess.format(self.train_id, delay_time))

    def delay_departure(self, delay_time, changes_time, train_mess):
        '''
        Delaying the departure for [delay_time]. Action happens at [changes_time]
        '''
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M')
        delta_dep = timedelta(
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
        self.__departure = self.departure + delta_dep
        schedule[changes_time].append(train_mess.format(self.train_id, delay_time))

    @abstractclassmethod
    def arrive(self):
        '''
        Accepting the train
        '''
        pass

    @abstractclassmethod
    def depart(self):
        '''
        Departing the train
        '''
        pass

    @abstractclassmethod
    def process_train(self):
        '''
        Running all the needed functions in order to process train
        '''
        pass
