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
        return self.items.pop()

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass


