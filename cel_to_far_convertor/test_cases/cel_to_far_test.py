#Importing the unittest module.
import unittest
#Importing the converter module.
from classes.converter import converter
#Creating the class.
class TestConverter(unittest.TestCase):
    """
    Creating a class for unittesting.
    """
    def setUp(self):
        """
        Creating an instance of the converter class.
        """
        #Creating an instance of the class.
        self.my_converter = converter(98.33)
    def test_celsius_fahrenheit_converter_assert_false(self):
        """
        Testing the celsius_fahrenheit_converter method
        """
        bad_list = ["98.22", "asa"," ", "", "342243", "34", "2",".3",".33", ".321",".sdsa", "dad.", "s.", ".y"]
        for bad in bad_list:
            self.assertFalse(self.my_converter.celsius_fahrenheit_converter(bad))
    def test_celsius_fahrenheit_converter_true(self):
        """
        Testing the celsius_fahrenheit_converter method
        """
# if __name__ == '__main__':
#     unittest.main()