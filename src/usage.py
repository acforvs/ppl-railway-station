USAGE = '''USAGE:
Schedule input:

MARKS:
* N —— amount of trains that arrives at the platfrom during the day
* M —— amount of events
* K —— amount of connections

FORMAT:
1st line: [day/month/year] —— date of the schedule 
2nd line: [N] [M] [K] —— amount of trains, events and connections
3rd line: [amount of platforms] [amount of ways]
K lines: [connection]
N lines: [train number] [amount of carriages] [train type]
M lines: [train number] [event]

CONNECTION DESCRIPTION (if platform and way are connected):
[platform number] [way number]

TRAIN TYPES:
P    :     passenger
F    :     freight
E    :     the train that destination / origin is the platfrom

POSSIBLE EVENTS:
1. add [amount] [time]    :    add [amount] of carriages in [time]
2. remove [amount] [time]    :    remove [amount] of carriages in [time]
3. schedule [arrival] [departure]    :    set the arrival & departure time 
format    :    day/month/year hours:minutes
4. delay arrival [minutes] [time]    :    delay the arrival for [minutes] minutes in [time]
5. delay departure [minutes] [time]    :    delay the departure for [minutes] minutes in [time]
'''

ARGUMENTS = '''
[-f]    :    set path to the schedule file
[-u]    :    usage
'''
