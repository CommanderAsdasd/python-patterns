# coding: utf-8

import random

class WarFabric(object):
	# animal_factory присваивается к None чтобы быть абстрактным и ничего не делать.
	def __init__(self, warriors_factory=None):
		self.pet_factory = warriors_factory


def droid():
	print("droid PEW")

def clone_stormtrooper():
	print("PEW")

clone_stormtrooper()
droid()