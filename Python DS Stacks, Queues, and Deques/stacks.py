class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """ Accepts an item as a parameter and appends it to the end of our list.
            Returns None
            Runtime: The runtime for this metyhod is O(1), or constant time, because
            appending to the end of the list happpens in constant time.
        """
        self.items.append(item)

    def pop(self):
        """ Return the last item from the list which is also the last item of the stack
            Runtime: The runtime for this method is O(1), or constant time, because all
            it does is index to the list item of the list .
        """
        if self.items:
            return self.items.pop()
        return None


    def peek(self):
        """ This  method returns the last item in the list. which is also item at the
            top of the stack. 
            Runtime: This method runs in constant time because indexing into a list is done
            in constant time 
        """
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        pass


