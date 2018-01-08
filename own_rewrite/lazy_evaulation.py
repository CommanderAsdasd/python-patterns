from __future__ import print_function
import functools

class lazy_property(object):

    def __init__(self, function):

        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val

class Person(object):

    def __init__(self, name, occupation):
        self.name = name
        # что ещё за оккупация
        self.occupation = occupation

    @lazy_property
    def relatives(self):
        # Get all relatives, let's assume it costc much time
        # There is lazyness come in play

def main():
    John = Person('John', 'Huy')
    print(u'Name: {0}  Occupation: {1}'.format(John.name, John.occupation))
    print(u"Before we access `relatives`:")
    print(John.__dict__)
    print(u"John's `relatives`: {}".format(John.relatives))
    print(u'We accessed `relatives`:')
    print(John.__dict__)

if __name__ == '__main__':
    main()