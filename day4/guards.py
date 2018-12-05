from datetime import datetime
import operator
import sys

class Event:
    def __init__(self, dt, data):
        self.dt = dt
        self.data = data

    def __str__(self):
        return '{} {}'.format(self.dt, self.data)

class State:
    def __init__(self):
        self.current_guard = -1
        self.is_asleep = False
        self.went_asleep = -1
        self.sleep_log = {}

def parse_event(string):
    timestamp = string[1:17]
    data = string[19:].strip()
    dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    return Event(dt, data)

def validate_events(events):
    is_asleep = False
    guard_id = -1
    i = 0
    while i < len(events):
        event = events[i]
        if event.data == 'wakes up':
            if not is_asleep:
                print('wake but not asleep {}'.format(i))
                events[i], events[i+1] = events[i+1], events[i]
                i += 1
            is_asleep = False
        elif event.data == 'falls asleep':
            if is_asleep:
                print('sleenew guard but asleep 135p but asleep {}'.format(i))
                events[i], events[i+1] = events[i+1], events[i]
                i += 1
            is_asleep = True
        else:
            if is_asleep:
                print('new guard but asleep {}'.format(i))
                events[i], events[i-1] = events[i-1], events[i]
                is_asleep = True
            guard_id = int(event.data.split(' ')[1][1:])
        i += 1

def handle_wake_up(state, minute):
    state.is_asleep = False
    log = state.sleep_log[state.current_guard] if state.current_guard in state.sleep_log else [0] * 60
    for i in range(state.went_asleep, minute):
        log[i] += 1
    state.sleep_log[state.current_guard] = log

def handle_falls_asleep(state, minute):
    state.is_asleep = True
    state.went_asleep = minute

def handle_new_guard(state, data):
    guard_id = int(data.split(' ')[1][1:])
    state.current_guard = guard_id

def main():
    events = []
    with open('input.txt') as file:
        for line in file:
            events.append(parse_event(line))

    events.sort(key=operator.attrgetter('dt'))

    validate_events(events)

    state = State()

    for event in events:
        if event.data == 'wakes up':
            handle_wake_up(state, event.dt.minute)
        elif event.data == 'falls asleep':
            handle_falls_asleep(state, event.dt.minute)
        else:
            handle_new_guard(state, event.data)

    total_sleep_times = dict(map(lambda kv: (kv[0], sum(kv[1])), state.sleep_log.items()))
    sleepiest_guard = max(total_sleep_times.items(), key=operator.itemgetter(1))[0]
    sleepiest_minute = max(enumerate(state.sleep_log[sleepiest_guard]), key=operator.itemgetter(1))[0]

    print('Sleepiest guard: {} Sleepiest minute: {}'.format(sleepiest_guard, sleepiest_minute))
    print('Final answer: {}'.format(sleepiest_guard * sleepiest_minute))

    frequent_sleep_times = dict(map(lambda kv: (kv[0], max(kv[1])), state.sleep_log.items()))
    consistent_sleepy_guard, amount_of_times_asleep = max(frequent_sleep_times.items(), key=operator.itemgetter(1))
    minute = state.sleep_log[consistent_sleepy_guard].index(amount_of_times_asleep)

    print('Consistant Sleepiest guard: {} Sleepiest minute: {}'.format(consistent_sleepy_guard, minute))
    print('Final answer: {}'.format(consistent_sleepy_guard * minute))

if __name__ == '__main__':
    main()

