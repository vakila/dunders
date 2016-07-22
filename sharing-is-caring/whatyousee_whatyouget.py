# Anders Hammarquist
# __new__ lets you return anything, not just
# instances of your class.

import json

# a class that turns into a string
class Stringify:

    def __new__(cls, *args):
        return ' '.join(map(str, args))


# Of course, you can go even crazier and
# do the same with the metaclass

class mJson(type):

    def __new__(mcls, name, bases, namespace):
        return json.dumps(namespace)


if __name__ == '__main__':
    mystring = Stringify([1,2,3,'a',object()])

    class MyJson(metaclass=mJson):
        answer = 42

    print('mystring = {}'.format(mystring))
    print('type(mystring) = {}'.format(type(mystring)))
    print('MyJson = {}'.format(MyJson))
    print('type(MyJson) = {}'.format(type(MyJson)))
