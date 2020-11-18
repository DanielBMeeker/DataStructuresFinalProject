"""
Program: Queue.py
Author: Daniel Meeker
Date: 9/27/2020

This program demonstrates creating a queue in Python with a list.
I may have gone about the logic differently than you intended but
in the end all my tests pass and I felt like I was adhearing to the
MERUSE principal of elegance.

I think all my logic issues I was having stems from me changing
the 'self.items = ["" for x in range(max_size)]' which I did because
that made my size function (and by extension my is_full() and is_empty())
easier to write but by doing that I changed the logic of enqueue and dequeue
to use .append() and .remove() rather than self.items[self.tail] = item. Sorry if this
isn't how you intended the lab to work but by the time I realized I wasn't able
to make self.head and self.tail work as intended I would have had to scrap all
the work I did and start over and since my tests were working I decided to leave it as-is.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""


class QueueFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class Queue:
    def __init__(self, max_size=5):
        self.head = 0
        # self.tail = 0 not used because of my use of the built-in remove function for
        # Python lists which adjusts the indexes of the queue automatically.
        self.queue_size = 0  # changed the name to self.queue_size because it was causing
        # errors with the size() function. I first tried changing the size function to a
        # property setter but ran into some maximum recursion errors.
        self.max_size = max_size  # used to limit size of Queue. Defaults to 5.
        self.items = []  # adjusted this so that instead a list of blank spaces it is just
        # an empty list so that I could more easily track the size of the queue

    def is_empty(self):
        """
        If there are no elements in the queue this will return true,
        otherwise it will return false
        :return: boolean
        """
        if self.size() == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        If the number of elements in the queue are equal to its self.max_size
        this will return true, otherwise it will return false.
        :return:
        """
        if self.size() == self.max_size:
            return True
        else:
            return False

    def enqueue(self, item):
        """
        This function will take an item and add it to the end of the queue
        I handled wrap around by using the Python list built in remove function
        in the dequeue function which automatically adjusts the indexes of each
        item in the queue so that this implementation doesn't have to worry
        about wrap around.
        :param item: required
        :return: void
        """
        if not self.is_full():
            self.items.append(item)
        else:
            raise QueueFullException("Queue is Full")

    def dequeue(self):
        """
        I was having issues with wrap around so I decided to
        use the Python list function list.remove(item) where item
        is equal to self.peek() so that it grabs the first element.
        I did it that way instead of using the pop() function so that
        when 'item = self.peek()' runs it will throw the QueueEmptyException.
        I thought it was an elegant solution and made my brain hurt less than
        trying to make wrap around work.

        :return: first item of whatever data type is in the list
        """
        try:
            item = self.peek()
            self.items.remove(item)
            return item
        except QueueEmptyException:
            raise QueueEmptyException("Queue is Empty")

    def peek(self):
        if not self.is_empty():
            item_str = self.items[self.head]
            return item_str
        else:
            raise QueueEmptyException("Queue is Empty")

    def size(self):
        self.queue_size = len(self.items)
        return self.queue_size

    def print_queue(self):
        if not self.is_empty():
            stack_str = ""
            for x in range(self.size()):
                stack_str += str(self.items[x]) + "\n"
            return stack_str
        else:
            raise QueueEmptyException("Queue is Empty")


if __name__ == '__main__':
    max_size = 3
    resting_rate_queue = Queue(max_size)
    active_rate_queue = Queue(max_size)
    resting_rate_queue.enqueue({'11/12': 77})
    resting_rate_queue.enqueue({'11/13': 81})
    resting_rate_queue.enqueue({'11/14': 75})
    print(resting_rate_queue.print_queue())
    try:
        resting_rate_queue.enqueue(80)
    except QueueFullException as qf:
        print(qf)
    print(resting_rate_queue.dequeue())
    print(resting_rate_queue.dequeue())
    print(resting_rate_queue.dequeue())
    try:
        print(resting_rate_queue.print_queue())
    except QueueEmptyException as qe:
        print(qe)
    resting_rate_queue.enqueue(80)
    print(resting_rate_queue.print_queue())
    print(resting_rate_queue.is_empty())
    print(resting_rate_queue.dequeue())
    print(resting_rate_queue.is_empty())
    try:
        print(resting_rate_queue.dequeue())
    except QueueEmptyException as qe:
        print(qe)
    input("Press Enter to End")
