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
        """ Removes and returns the item in the 0th index of the list, 
            which represents the front of the deque.
            The runtime is linear,  or O(N), because when we remove an item
            from the 0th index, all the other items have to shift one index to the left
        """
        if self.items:
            return self.items.pop(0)
        return None


    def remove_rear(self):
        """ Removes and returns the last item of the list, which representst the rear of
            the deque. 
            Runtime is constant time because all we're doing is indexing to the end of a
            list and removing the last item
        """
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        """ Returns the value found at the 0th index of the list, which represents
            the front of the deque.
            Runtime: is O(1)/constant because all we are doing is indexing into a list.
        """
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        """ Retuns the value found at end of the list which represents the rear
            of the deque.
            Runtime: is O(1)/ constant because all we are doing is indexing into a list
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        pass

    def is_empty(self):
        pass
