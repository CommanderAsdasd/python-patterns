#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random

class PetShop(object):

    """a pet shop"""

    def __init__(self, animal_factory=None):
        """init startup factory. Init factory with none default"""

        self.pet_factory = animal_factory

    def show_pet(self):
        """creates and shows a pet using abstract factory. Show pet used like - take methods from given object with it's methods"""

        pet = self.pet_factory.get_pet()
        print("Appeared {}".format(pet))
        print("It says {}".format(pet.speak()))
        print("We also have {}".format(self.pet_factory.get_food()))

"""implement some look similar classes"""

class Dog(object):


    def speak(self):
        return "Woof"

    def __str__(self):
        return "Dog"

class Cat(object):

    def speak(self):
        return "Meow"

    def __str__(self):
        return "Cat"

# Factories

class DogFactory(object):

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"

class CatFactory(object):

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat food"

def get_factory():
    """dynamic on it's nature"""
    return random.choice([DogFactory, CatFactory])()

if __name__ == "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

###