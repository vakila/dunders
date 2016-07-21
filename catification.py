# Anjana Vakil
# "Using and abusing Python's double-underscore methods and attributes"
# EuroPython 2016
#
# License: Don't use this code for anything, ever! :)
# (But if you do, give credit where credit is due.)

import time

## A boring normal function with a docstring
def add(spam, eggs):
    '''A boring function that sums two integers.'''
    return spam + eggs



## Hacking with function object dunders!
def catify(fn):
    '''Hacks a function to be more feline'''
    def moar_tuna(*args):
        print("give meow moar tuna plz!")
        return "pu" + "r" * sum(args)
    fn.__doc__ = "meow!"
    fn.__code__ = moar_tuna.__code__



## Context manager to be used with `with`
class CatsInChargeOf:

    def __init__(self, fn):
        '''Just hanging on to some boring data
        in case we need it later...
        '''
        self.boring_human_fn = fn
        self.boring_code = fn.__code__
        self.boring_doc = fn.__doc__

    def __enter__(self):
        '''Called when we enter `with` block'''
        self.reign_begins = time.time()
        catify(self.boring_human_fn)
        return self

    def __exit__(self, *exc):
        '''Called when we exit the `with` block,
        even if there was an exception `exc`.
        '''
        self.reign_ends = time.time()
        self.boring_human_fn.__doc__ = self.boring_doc
        self.boring_human_fn.__code__ = self.boring_code
        print("\nFeline rule ended after {:.2f} glorious seconds"
              .format(self.reign_ends - self.reign_begins))


if __name__ == "__main__":

    # add works normally...
    add(2,3)

    # then along come the cats...
    with CatsInChargeOf(add):
        add(2,3)
        add(4,5)
        add(6,7)

    # but once they've left, all is normal!
    add(2,3)
