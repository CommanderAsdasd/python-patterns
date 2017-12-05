#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__= self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state

class YourBorg():
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))
    print(rm1.__dict__)

    rm1.state = 'lol_state'
    
    print('rm1: {0}'.format(rm1))
    print('rm2: {0}'.format(rm2))