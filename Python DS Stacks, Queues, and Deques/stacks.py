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
        return self.items[-1]

    def size(self):
        pass

    def is_empty(self):
        pass


