# the deque = Double-Ended queue
class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        """ Takes an item as a parameter and inserts it into the zeroth index of the
            list that is representing the deque 
            Runtime: is linear or O(N), or linear, as all the other items in the
            list need to shift one position to the right.
        """
        self.items.insert(0, item)

    def add_rear(self, item):
        """ Takes in an item as a parameter and appends that item to the end of the list
            that is representing the deque.
            The runtime is constant time because appending to the end of the list
            happens in constant time 
        """
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)


    def remove_rear(self):
        return self.items.pop()

    def peek_front(self):
        pass

    def peek_rear(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass
