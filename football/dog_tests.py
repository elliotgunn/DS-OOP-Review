import unittest
from dog import Dog


class DogTest(unittest.TestCase):

    def setUp(self):
        self.default_dog = Dog()
        self.custom_dog = Dog(name='Mickey', species='Lab')

    def test_defaults(self):
        self.assertEqual(self.default_dog.name, 'Spot')
        self.assertEqual(self.default_dog.species, 'Dalmation')
        self.assertEqual(self.custom_dog.name, 'Mickey')
	self.assertEqual(self.custom_dog.species, 'Lab')

    def test_bark(self):
        self.assertEqual(self.default_dog.bark(), 'Woof!')
        self.assertEqual(self.custom_dog.bark(), 'Woof!')

    def test_run(self):
        self.assertEqual(self.default_dog.run(), 'Vroom!')  # Doesn't work! Printing is a side effect


if __name__ == '__main__':
    unittest.main()
