from model import queue
from model.map import MapMeeker as map
from datetime import datetime

if __name__ == '__main__':
    resting_rate_queue = queue.Queue()
    active_rate_queue = queue.Queue()
    more_input = True
    while more_input:
        resting_map = map()
        active_map = map()
        date = input("Enter the date")
        resting_rate = input("Enter resting rate")
        active_rate = input("Enter active rate")
        more_input = input("Y/N, more input?")
        if more_input.upper() == 'N':
            more_input = False
        else:
            more_input = True
        resting_map.insert(date, resting_rate)
        active_map.insert(date, active_rate)
        active_rate_queue.enqueue(active_map)
        resting_rate_queue.enqueue(resting_map)
    print(active_rate_queue.print_queue())
