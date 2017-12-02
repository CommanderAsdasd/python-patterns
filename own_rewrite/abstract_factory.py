import random

class PetShop(object):

    """a pet shop"""

    def __init__

    def show_pet

class Dog(object):

    def speak(self):

    def __str__(self):

class Cat(object):

    def speak(self)

    def __str__(self)

# Factories

class DogFactory(object):

    def get_pet(self)

    def get_food(self)

class CatFactory(object):

    def get_pet()

    def get_food()

def get_factory():
    """dynamic on it's nature"""

if __name__ = "__main__":
    for i in range(3):
        shop = PetShop(get_factory())
        shop.show_pet()
        print("=" * 20)

###