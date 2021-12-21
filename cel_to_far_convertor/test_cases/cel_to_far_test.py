#Importing the unittest module.
import unittest
#Importing the converter module.
from classes.converter import converter
#Creating the class.
class TestConverter(unittest.TestCase):
    def __init__(self):
        """
        Creating an instance of the converter class.
        """
        #Creating an instance of the class.
        my_converter = converter(98.33)
    def test_celcius_fahrenheit_converter_false(self):
        """
        
        """