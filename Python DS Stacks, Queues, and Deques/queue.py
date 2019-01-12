# Class for queue data structure

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """ Takes in an item and inserts that item into the 0th index
            of the list that is representing the Queue.

            Runtime: The runtime is O(n), or linear time because inserting into the 0th 
            index of the list forces all the other items in the list to move one index to
            the right 
        """
        self.itmes.insert(0, item)

    def dequeu(self):
        """ Returns and removes the first most item of the queue, which is represented by
            the last item in the list.
            Runtime: The runtime is O(1), because indexing to the end of a list happens in
            constant time.
        """
        if self.items:
            self.items.pop()
        return None

    def peek(self):
        """ Returns the last item in the list, which represents the first item
            in the queue
            Runtime: is constant time because we are just indexing ]
            to the last item of the list
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        pass

    def is_empty(self):
        pass
