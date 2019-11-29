import logging
from abc import ABC, abstractmethod
from typing import Dict

logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', 
                    level=logging.DEBUG,
                    datefmt='%d/%m/%Y %H:%M:%S')

TracksOccup = Dict[int, bool] 
Track2Platfrom = Dict[int, int]

class Platforms():
    '''Documentaion goes here.
    '''
    def __init__(self, platforms_count):
        self.platforms_count = platforms_count
    
    def __str__(self):
        return F'''
        Platforms.
        There are {self.platforms_count} platforms at the station'''
    
    @abstractmethod
    def set_platform(self, train_id, time, platform_num):
        pass

    @abstractmethod
    def leave_platform(self, train_id, time, platform_num):
        pass

class RailTracks():
    '''Documentation goes here.
    '''
    def __init__(self, tracks_count: int=None, tracks_status: TracksOccup=None, tracks2platforms: Track2Platfrom=None):
        if not tracks_count:
            self.__tracks_count = 0
        else:
            self.__tracks_count = tracks_count

        if not tracks_status:
            self.__tracks_status = {}
        else:
            self.__tracks_status = tracks_status

        if not tracks2platforms:
            self.__tracks2platforms = {}
        else:
            self.__tracks2platforms = {}

    
    def __str__(self):
        return F'''
        RailTracks.
        There are {self.__tracks_count} tracks at the station'''

    # Getters section begin
    @property
    def tracks_count(self) -> int:
        return self.__tracks_count
    
    @property
    def tracks_status(self) -> TracksOccup:
        return self.__tracks_status

    @property
    def tracks2platforms(self) -> Track2Platfrom:
        return self.__tracks2platforms
    # Getters section end

    def connect(self, track_num, platform_num):
        logging.debug(F'connect() called with the {track_num, platform_num} arguments')
        self.__tracks2platforms[track_num] = platform_num
           
    def update_status(self, track_num):
        logging.debug(F'update_status() called with the {track_num} argument')
        self.__tracks_status[track_num] = not self.__tracks_status[track_num]

    


