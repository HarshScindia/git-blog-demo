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
    def __init__(self, items):

