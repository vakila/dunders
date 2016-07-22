"""
Using getters & setters with the equality dunder
for checking hashed passwords in a database model so
you can validate if the input that a user gave you
is a valid password.

So you can do this:

    user.password == input_password

Instead of:

    input_hash = hash_lib.hash(input_passwd)
    user.password_hash == input_hash
"""

import hashlib


class Password:

    def __init__(self, user):
        self.user = user

    def __eq__(self, other):
        return self.user.password_hash == self.__hashit(other)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Hash: {}".format(self.user.password_hash)

    def __hashit(self, passwd):
        hasher = hashlib.new("sha1")
        hasher.update(passwd.encode("utf_8"))
        return hasher.hexdigest()

    def set(self, new):
        self.user.password_hash = self.__hashit(new)


# ORM object
class User:

    def __init__(self):
        # This is stored at the db
        self.password_hash = ""
        # This won't
        self.__password = Password(self)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, passwd):
        self.__password.set(passwd)


if __name__ == '__main__':
    user = User()
    user.password = "1234"
    print(
        "`{}` equals `{}`: {}"
        .format(
            user.password,
            "1234",
            user.password == "1234"
    ))
