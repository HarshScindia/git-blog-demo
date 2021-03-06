# The Print Queue Challenge
""" Create 3 classes that, together, model how a printer could take print jobs
    out of aq print queue.
    Requirements
    PrintQueue class that follows the queue data structure implementation.
    Job class pages attribute - random 1 to 10
        print_page() - decrement pages
        check_complete() - which will check wether all the pages are printed
    Printer Class - 
        get_job() - account for the case where
        PrintQueue.items is empty
        print_job() """

class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def deque(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]

    def size(self):
        return len(self.itmes)

    def is_empty(self):
        return self.items == []


class Job:
    def __init__(self):
        self.pages = 0

    def print_pages(self):
        pass

    def check_complete(self):
        pass


class Printer:
    def __init__(self):
        pass

    def get_job(self):
        pass

    def print_job(self):
        pass
