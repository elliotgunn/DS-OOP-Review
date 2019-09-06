"""
Class to represent Dogs!
"""


class Dog:
  
    def __init__(self, name='Spot', species='Dalmation'):
       self.name = name
       self.species = species

    def run(self):
       print('Vroom!')

    def bark(self):
       return 'Woof!'


