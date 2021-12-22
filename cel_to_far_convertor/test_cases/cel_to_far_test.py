#Importing the unittest module.
import unittest
#Importing the converter module.
from classes.converter import converter
#Creating the class.
class TestConverter(unittest.TestCase):
    """
    Creating a class for unittesting.
    """
    def setup(self):
        """
        Creating an instance of the converter class.
        """
        #Creating an instance of the class.
        my_converter = converter(98.33)
    def test_celsius_fahrenheit_converter_false(self):
        """
        Testing the celsius_fahrenheit_converter method
        """
        bad_list = ["98.22", "asa"," ", "", "342243", "34", "2",".3",".33", ".321",".sdsa", "dad.", "s.", ".y"]
    def test_celsius_fahrenheit_converter_true(self):
        """
        Testing the celsius_fahrenheit_converter method
        """
if __name__ == '__main__':
    unittest.main()