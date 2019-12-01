from read import read
from data import schedule, events, trains

def main():
    read()
    for event in events:
        if (event.description[0] == 'add'):
            trains[event.id].add_carriages(int(event.description[1]), event.description[2] + ' ' + event.description[3])
        if (event.description[0] == 'remove'):
            trains[event.id].remove_carriages(int(event.description[1]), event.description[2] + ' ' + event.description[3])
        if (event.description[0] == 'schedule'):
            arrival = event.description[0] + ' ' + event.description[1]
            departure = event.description[2] + ' ' + event.description[2]
            train = trains[event.id]
            train.set_arrival(arrival)
            train.set_departure(departure)
            train.process_train()
        if (event.description[0] == 'delay'):
            minutes = event.description[3]
            changes_time = event.description[4] + ' ' + event.description[5]
            if (event.description[1] == 'arrival'):
                trains[event.id].delay_arrival(minutes, changes_time)
            if (event.description[1] == 'departure'):
                trains[event.id].delay_departure(minutes, changes_time)
    with open('/Users/vladislavsavinov/Projects/ppl-railway-station-acforvs/src/out.txt', 'w') as out:  
        for key in schedule.items():
            print(key[0], key[1], file=out)

if __name__ == '__main__':
    main()
