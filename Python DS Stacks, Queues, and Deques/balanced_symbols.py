"""
Create a function that takes in a string of symbol pairs as a parameter.

The function should return True if the symbol string is balanced or False if it is not.

# Requirements
    The string should only contain opening and closing symbols, like '([{}])' or '(([{])'.

    For symbols to be balanced, each opening symbol must also have a closing symbol, and 
    the symbol must also have a closing symbol, and the symbols must be properly nested.

    Make use of a stack in your solution.
    
    Example Balanced symbols
    ([{}])
    ([]{}())
    (((((())))))

    Unbalanced Symbols

    (([{])
    [}([){]
"""
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        if self.items:
            self.items.pop()

    def peek(self):
        if self.items:
            self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

def balanced_symbols(symbol_string):
    balanced = False
    balance_stack = Stack()
    symbol_list symbol_string.split()
    for i in symbol_list:
        if i == '(' or '{' or '[':
            balance_list.push(i)
        elif i == ')' or '}' or ']':
            if i == balance_stack.peek():
                balance_stack.pop()
            else:
                balance_stack.push(i)
