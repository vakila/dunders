# Anjana Vakil
# "Using and abusing Python's double-underscore methods and attributes"
# EuroPython 2016
#
# License: Don't use this code for anything, ever! :)
# (But if you do, give credit where credit is due.)


## A dunder-ful class!
class StringyInt:

    ## Basic dunders
    def __init__(self, value):
        '''The beloved constructor method!'''
        self.value = value

    def __str__(self):
        '''Returns a "user-friendly" string representation
        of the object, for e.g. printing.
        '''
        return "ZOMG it's {} y'all!!!".format(self.value)

    def __repr__(self):
        '''Returns a representation of self "as code",
        usually as something that Python
        could understand and evaluate.
        '''
        return str(self.value)

    ## Operator overloading dunders
    def __add__(self, other):
        '''Called by the + operator on the left-hand object.'''
        new_value = int(str(self.value) + str(other.value))
        return StringyInt(new_value)

    def __mul__(self, other):
        '''Called by the * operator on the left-hand object.'''
        return StringyInt(int(str(self.value) * other.value))

    def __radd__(self, other):
        '''Called by the + operator on the right-hand object,
        if __add__ is not supported (for the given types)
        for the left-hand obj.
        '''
        return StringyInt(other).__add__(self)


    def __eq__(self, other):
        '''Called by ==, and also used for hashing
        keys into a dict (see __hash__ below).'''
        try:
            return self.value == other.value
        except AttributeError:
            return self.value == int(other)

    ## Hashability dunder
    def __hash__(self):
        '''In combination with __eq__,
        makes the object hashable,
        e.g. for use as a key in a dict.
        Only for immutables!
        '''
        return self.value

    ## Prevents creation of __dict__, saves time & space
    __slots__ = ('value')


## Some old dunder friends:
if __name__ == "__main__":
    # This block is executed only if the module is run
    # (not if it's imported)

    # Setting up some fun new objects to play with:
    one = StringyInt(1)
    two = StringyInt(2)
    three = StringyInt(3)

    # Run this module in interactive mode and play around!














#
