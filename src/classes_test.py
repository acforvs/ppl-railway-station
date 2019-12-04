import pytest
import random
from itertools import repeat
from datetime import datetime, timedelta
from passenger_train import PassengerTrain
from freight_train import FreightTrain
from formed_train import FormedTrain
from data import initialize, schedule
from messages import PASSENGER_DELAY_ARRIVAL, PASSENGER_DELAY_DEPARTURE, \
    PASSENGER_ARRIVAL, PASSENGER_DEPARTURE, \
        FORMED_DELAY_ARRIVAL, FORMED_DELAY_DEPARTURE, \
            FREIGHT_ARRIVAL, FORMED_ARRIVAL

pass_train = PassengerTrain(train_id=10, carriage_num=20)
fr_train = FreightTrain(train_id=10, carriage_num=20)
form_train = FormedTrain(train_id=10, carriage_num=20)

def generate_time():
    hours, minutes = str(random.randint(0, 23)), str(random.randint(0, 59))
    if len(hours) == 1:
        hours = '0' + hours
    if len(minutes) == 1:
        minutes = '0' + minutes
    time = hours + ':' + minutes
    return time


def test_delay_arrival_passenger():
    date = '14/03/2011'
    initialize(date)
    expected = []
    real_data = []

    for _ in repeat(None, 100000):
        time = generate_time()
        arrival_value = date + ' ' + time
        pass_train.set_arrival(arrival_value)

        delta_changes = timedelta(minutes=random.randint(0, 30))
        delta_arrival = random.randint(1, 59)
        changes_time = pass_train.arrival - delta_changes
        pass_train.delay_arrival(int(delta_arrival), changes_time.strftime('%d/%m/%Y %H:%M'))

        expected.append(PASSENGER_DELAY_ARRIVAL.format(pass_train.train_id, delta_arrival))
        for x in schedule[changes_time]:
            real_data.append(x)
    
    assert set(expected) == set(real_data)

def test_delay_departure_passenger():
    date = '08/09/2001'
    initialize(date)
    expected = []
    real_data = []

    for _ in repeat(None, 100000):
        time = generate_time()
        departure_value = date + ' ' + time
        pass_train.set_departure(departure_value)

        delta_changes = timedelta(minutes=random.randint(0, 30))
        delta_departure = random.randint(1, 59)
        changes_time = pass_train.departure - delta_changes
        pass_train.delay_departure(int(delta_departure), changes_time.strftime('%d/%m/%Y %H:%M'))

        expected.append(PASSENGER_DELAY_DEPARTURE.format(pass_train.train_id, delta_departure))
        for x in schedule[changes_time]:
            real_data.append(x)
    
    assert set(expected) == set(real_data)

def test_delay_arrival_formed():
    date = '14/03/2011'
    initialize(date)
    expected = []
    real_data = []

    for _ in repeat(None, 100000):
        time = generate_time()
        arrival_value = date + ' ' + time
        form_train.set_arrival(arrival_value)

        delta_changes = timedelta(minutes=random.randint(0, 30))
        delta_arrival = random.randint(1, 59)
        changes_time = form_train.arrival - delta_changes
        form_train.delay_arrival(int(delta_arrival), changes_time.strftime('%d/%m/%Y %H:%M'))

        expected.append(FORMED_DELAY_ARRIVAL.format(form_train.train_id, delta_arrival))
        for x in schedule[changes_time]:
            real_data.append(x)
    
    assert set(expected) == set(real_data)

def test_delay_departure_formed():
    date = '08/09/2001'
    initialize(date)
    expected = []
    real_data = []

    for _ in repeat(None, 100000):
        time = generate_time()
        departure_value = date + ' ' + time
        form_train.set_departure(departure_value)

        delta_changes = timedelta(minutes=random.randint(0, 30))
        delta_departure = random.randint(1, 59)
        changes_time = form_train.departure - delta_changes
        form_train.delay_departure(int(delta_departure), changes_time.strftime('%d/%m/%Y %H:%M'))

        expected.append(FORMED_DELAY_DEPARTURE.format(form_train.train_id, delta_departure))
        for x in schedule[changes_time]:
            real_data.append(x)
    
    assert set(expected) == set(real_data)

def test_arrive_passenger():
    date = '07/05/1980'
    initialize(date)
    expected = []
    real_data = []

    for _ in repeat(None, 1000):
        time = generate_time()
        arrival_value = date + ' ' + time
        pass_train.set_arrival(arrival_value)
        pass_train.arrive()

        expected.append(PASSENGER_ARRIVAL.format(pass_train.train_id))
        for x in schedule[pass_train.arrival]:
            real_data.append(x)
    
    assert set(expected) == set(real_data)

def test_arrive_freight():
    date = '14/03/1972'
    initialize(date)
    expected = []
    real_data = []

    for _ in repeat(None, 1000):
        time = generate_time()
        arrival_value = date + ' ' + time
        fr_train.set_arrival(arrival_value)
        fr_train.arrive()

        expected.append(FREIGHT_ARRIVAL.format(fr_train.train_id))
        for x in schedule[fr_train.arrival]:
            real_data.append(x)
    
    assert set(expected) == set(real_data)
