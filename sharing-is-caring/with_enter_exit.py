
class Login:
    def __init__(self, user, password):
        self._user = user
        self._password = password
        self.__accounts = {'arthur': 'asd123', 'admin': 'admin'}
        self.__authenticated = False

    def __enter__(self):
        successful = self.__accounts.get(self._user, None) == self._password
        self.__authenticated = successful
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__authenticated = False

    def hello(self):
        if self.__authenticated:
            return 'Welcome, ' + self._user
        return 'Access denied'


if __name__ == '__main__':
    with Login('arthur', 'asd123') as login:
        print('Inside  "with Login": ' + login.hello())
    print('Outside "with Login": ' + login.hello())
