from abc import ABC, abstractclassmethod
from datetime import datetime, timedelta
import logging
from data import schedule, availability
from strings import PASSENGER_DELAY_ARRIVAL, PASSENGER_DELAY_DEPARTURE, \
    PASSENGER_WAY, PASSENGER_PLATFORM, \
    PASSENGER_ARRIVAL, PASSENGER_DEPARTURE, \
    FREIGHT_ARRIVAL, FREIGHT_DELAY_ARRIVAL, \
    FREIGHT_PLATFORM, FREIGHT_WAY, \
    FORMED_DELAY_ARRIVAL, FORMED_DELAY_DEPARTURE, \
    FORMED_WAY, FORMED_PLATFORM, \
    FORMED_ARRIVAL, FORMED_DEPARTURE

logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s',
                    level=logging.DEBUG,
                    datefmt='%d/%m/%Y %H:%M:%S')


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
        self.arrival = datetime.combine(
            arrival_input.date(), arrival_input.time())
        departure_input = datetime.strptime(departure, '%d/%m/%Y %H:%M')
        self.departure = datetime.combine(
            departure_input.date(), departure_input.time())
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

    # okay I can change the name but you have to check this
    # https://en.wikipedia.org/wiki/L%27Arrivée_d%27un_train_en_gare_de_La_Ciotat
    # out
    @abstractclassmethod
    def L_arrivée_d_un_train(self):
        pass

    @abstractclassmethod
    def depart(self):
        pass

    @abstractclassmethod
    def process_train(self):
        pass


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
        schedule[self.arrival] = PASSENGER_ARRIVAL.format(self.id)

    def set_platform(self, platform_num):
        self.platform = platform_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time] = PASSENGER_PLATFORM.format(
            self.id, self.platform, self.arrival)

    def set_way(self, way_num):
        self.way = way_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time] = PASSENGER_WAY.format(self.id, self.way)

    def delay_arrival(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time //
            1440,
            hours=(
                delay_time -
                delay_time %
                1440) //
            60,
            minutes=delay_time %
            60)
        self.arrival = self.arrival + delta
        schedule[changes_time] = PASSENGER_DELAY_ARRIVAL.format(self.id, delta)

    def delay_departure(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time //
            1440,
            hours=(
                delay_time -
                delay_time %
                1440) //
            60,
            minutes=delay_time %
            60)
        self.departure = self.departure + delta
        schedule[changes_time] = PASSENGER_DELAY_DEPARTURE.format(
            self.id, delta)

    def depart(self):
        schedule[self.departure] = PASSENGER_DEPARTURE.format(self.id)


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
        schedule[self.arrival] = FREIGHT_ARRIVAL.format(self.id)

    def set_platform(self, platform_num):
        self.platform = platform_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time] = FREIGHT_PLATFORM.format(
            self.id, self.platform, self.arrival)

    def set_way(self, way_num):
        self.way = way_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time] = FREIGHT_WAY.format(self.id, self.way)

    def depart(self):
        raise ValueError('''The freight train should stay here a little longer.
                            There is no depart() func for this train''')


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
        schedule[self.departure] = FORMED_ARRIVAL.format(self.id)

    def set_platform(self, platform_num):
        self.platform = platform_num
        delta = timedelta(minutes=30)
        setting_time = self.arrival - delta
        schedule[setting_time] = FORMED_PLATFORM.format(self.id, self.platform)

    def set_way(self, way_num):
        self.way = way_num
        delta = timedelta(minutes=10)
        setting_time = self.arrival - delta
        schedule[setting_time] = FORMED_WAY.format(self.id, self.way)

    def delay_arrival(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time //
            1440,
            hours=(
                delay_time -
                delay_time %
                1440) //
            60,
            minutes=delay_time %
            60)
        self.arrival = self.arrival + delta
        schedule[changes_time] = FORMED_DELAY_ARRIVAL.format(self.id, delta)

    def delay_departure(self, delay_time, changes_time):
        changes_time = datetime.strptime(changes_time, '%d/%m/%Y %H:%M').time()
        delta = timedelta(
            days=delay_time //
            1440,
            hours=(
                delay_time -
                delay_time %
                1440) //
            60,
            minutes=delay_time %
            60)
        self.departure = self.departure + delta
        schedule[changes_time] = FORMED_DELAY_DEPARTURE.format(self.id, delta)

    def depart(self):
        schedule[self.departure] = FORMED_DEPARTURE.format(self.id)
