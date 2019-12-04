from read import read
from data import schedule, events, trains
from messages import PASSENGER_DELAY_ARRIVAL, PASSENGER_DELAY_DEPARTURE, \
    FORMED_DELAY_DEPARTURE, FORMED_DELAY_ARRIVAL, \
        SEPARATOR

def main():
    read()
    for event in events:
        if (event.description[0] == 'add'):
            trains[event.id].add_carriages(int(event.description[1]), event.description[2] + ' ' + event.description[3])
        if (event.description[0] == 'remove'):
            trains[event.id].remove_carriages(int(event.description[1]), event.description[2] + ' ' + event.description[3])
        if (event.description[0] == 'schedule'):
            arrival = event.description[1] + ' ' + event.description[2]
            departure = event.description[3] + ' ' + event.description[4]
            train = trains[event.id]
            train.set_arrival(arrival)
            train.set_departure(departure)
            train.process_train()
        if (event.description[0] == 'delay'):
            minutes = int(event.description[2])
            changes_time = event.description[3] + ' ' + event.description[4]
            if (event.description[1] == 'arrival'):
                trains[event.id].delay_arrival(minutes, changes_time)
            if (event.description[1] == 'departure'):
                trains[event.id].delay_departure(minutes, changes_time)

    with open('/Users/vladislavsavinov/Projects/ppl-railway-station-acforvs/src/out.txt', 'w') as out:  
        for key in schedule.items():
            date = key[0]
            messages_list = key[1]
            print(date, file=out)
            if not messages_list:
                print("Nothing happend", file=out)
                print(SEPARATOR, file=out)
                continue
            for message in messages_list:
                print(message, file=out)   
            print(SEPARATOR, file=out)

if __name__ == '__main__':
    main()
