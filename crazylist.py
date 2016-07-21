# Anjana Vakil
# "Using and abusing Python's double-underscore methods and attributes"
# EuroPython 2016
#
# License: Don't use this code for anything, ever! :)
# (But if you do, give credit where credit is due.)

import random

def coin_flip():
    '''A little craziness helper.'''
    return random.random() > 0.5

class CrazyList:

    ## Some basic dunders, again
    def __init__(self):
        self.values = []

    def __repr__(self):
        return str(self.values)

    ## The craziness begins:
    def append(self, val):
        self.values.insert(random.randint(0, len(self.values)), val)

    ## Dunders for length and truthiness
    def __len__(self):
        '''Called by `len()`, and can also be called
        by `if obj` if `__bool__` isn't defined.
        '''
        return random.randint(0, 2*len(self.values))

    def __bool__(self):
        '''Called for e.g. `if obj: ...`'''
        return coin_flip()

    ## Dunders for iterables
    def __iter__(self):
        '''Used for `for` loops, and can be used
        for membership tests (e.g. `if x in obj: ...`).
        '''
        print("__iter__ got called!")
        for _ in range(len(self)):
            yield random.choice(self.values) if coin_flip() else '?'

    def __str__(self):
        '''Our old friend for `print()` etc.'''
        # the `for` loop here uses `__iter__`
        return str([v for v in self])

    ## Dunders for indexed/keyed objects
    def __getitem__(self, i):
        '''Called for obj[i] or obj[key],
        and can also be called by `for` loops
        or to test for membership (`x in obj`)
        if the object doesn't have
         `__iter__` and/or `__contains__`.
        '''
        return random.choice(self.values)

    def __setitem__(self, i, value):
        '''Used for obj[i] = x or obj[key] = value'''
        new_i = random.randint(0, len(self.values)-1)
        self.values[new_i] = value

    ## Dunder for membership
    def __contains__(self, item):
        '''Called by `x in obj`. Can be faster
        than the `__iter__`/`__getitem__` fallback.
        '''
        truth = item in self.values
        return truth if coin_flip() else not truth


if __name__ == "__main__":
    # A crazy little list for you to play with:
    l = CrazyList()
    for v in range(5):
        l.append(v)

    # Run this module in interactive mode and play around!
