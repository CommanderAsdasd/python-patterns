#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Lol():
    def kek(self):
        print("keksimus maximus")

A = Lol()
"Эта штука возвращает метод класса, указанный строкой. Этот метод потом можно вызвать"
print(getattr(A, "kek")())

class Gettattr_test():
    def __getattr__(self, attr):
        print("Huy tebe {}".format(attr))

B = Gettattr_test()

B.test