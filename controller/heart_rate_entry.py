from model import queue
from model.map import MapMeeker as map
from datetime import datetime

if __name__ == '__main__':
    more_input = True
    while more_input:
        date = input("Enter the date")
        resting_rate = input("Enter resting rate")
        active_rate = input("Enter active rate")
        more_input = input("Y/N, more input?")
        if more_input.upper() == 'N':
            more_input = False
        else:
            more_input = True
        resting_map = map()
        active_map = map()
        resting_map.insert(date, resting_rate)
        active_map.insert(date, active_rate)
    DAYS = resting_map.size()
    resting_rate_queue = queue.Queue(DAYS)
    active_rate_queue = queue.Queue(DAYS)
    for i in range(DAYS):
        active_rate_queue.enqueue(active_map.items()[i])
        resting_rate_queue.enqueue(resting_map.items()[i])
    print(active_rate_queue.print_queue())
