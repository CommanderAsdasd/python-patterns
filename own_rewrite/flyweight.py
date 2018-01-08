#!/usr/bin/env python
# -*- coding: utf-8 -*-

import weakref

"""Это приспособленец

Класс FlyiweightMeta делает что?"""
class FlyweightMeta(type):

    def __new__(mcs, name, parents, dct):

        """
        setup object pool
        """

        dct['pool'] = weakref.WeakValueDictionary()
        return super(FlyweightMeta, mcs).__new__(mcs, name, parents, dct)

    @staticmethod
    def _serialize_params(cls, *args, **kwargs):
        """
        serialize input parameters to a key.
        Simple implementation is just to serialize it as a string
        """
        gs_list = list(map(str, args))
        gs_list.extend([str(kwargs), cls.__name__])
        y = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serialize_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if not instance:
            instance = super(FlyweightMeta, cls).__call__(*args, **kwargs)
            pool[key] = instance
        return instance

class Card(object):

    """the object pool. Has builtin reference counting"""
    _CardPool = weakref.WeakValueDictionary()

    """Flyweight implementation. If the object exists in the pool 
    just return it (instead of creting new)"""
    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value + suit)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __repr__(self):
        return "<Card: %s%s>" % (self.value, self.suit)


def with_metaclass(meta, *bases):
    """Provide python metaclass compatibility"""
    return meta("NewBase", bases, {})

class Card2(with_metaclass(FlyweightMeta)):
    # print('Init {} : {})


if __name__ == '__main__':
    # comment __new__ and uncomment __init__ to see the difference
    c1 = Card('9', 'h')
    print(c1, c2)
    print(c1 == c2, c1 is c2)
    print(id(c1), id(c2))

    c1.temp = None 
    c3 = Card('9', 'h')
    print(hassattr(c3, 'temp'))

    # Tests with metaclass
    instances_pool = getattr(Card2, 'pool')
    cm1 = Card2('10', 'h', a=1)
    cm2 = Card2('10', 'h', a=1)
    cm3 = Card2('10', 'h', a=2)

    assert (cm1 == cm2) != cm3
    assert (cm1 is cm2) is not cm3
    asser len(instances_pool) == 2

    del cm1
    assert len(instances_pool) == 2

    del cm2
    assert len(instances_pool) == 1

