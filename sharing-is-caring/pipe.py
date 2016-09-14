import string
import operator


class Pipe:
    def __init__(self, iterable):
        self.iterable = iterable

    def __or__(self, func):
        """
        We recieve a function that will be applied to each value on the Pipe's iterable
        """
        iterable = (func(i) for i in self.iterable)

        # we return a new Pipe with the new iterable! (which is actually a generator!)
        return Pipe(iterable)

    def __repr__(self):
        return "Pipe(%s)" % self.iterable

    def __iter__(self):
        """
        The Pipe will yield the resulting iterable
        """
        return iter(self.iterable)

    def __rshift__(self, func):
        """
        Pipe() >> func(x,y)
        """
        return reduce(func, self.iterable)

    def __rlshift__(self, func):
        """
        func(iterable) << Pipe()
        """
        return func(self.iterable)


if __name__ == '__main__': 

    words = Pipe(["ONE", "TWO", "THREE"])

    bold = lambda s: '*{}*'.format(s)

    # Map
    for word in (words | string.lower | bold):
        print word

    # Reduce
    print (words | len) >> operator.add

    # Call iterable result
    print sum << (words | len)
