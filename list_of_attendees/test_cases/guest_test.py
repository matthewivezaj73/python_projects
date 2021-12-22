#Importing the unittest module.
import unittest
#Importing the Guests module.
from classes.validate_guests import Guests
#Creating the class.
class TestCrypto(unittest.TestCase):
    """
    Creating a class for unittesting.
    """
    def setup(self):
        """
        Creating an instance of the Guests class.
        """
        #Creating an instance of the class.
        my_guest = Guests("Sally", 22, 8374734624, "Guest")
    def test_validate_guest_age_false(self):
        """
        A unittest to test the age of the guest.

        Test conducted:
        assertFalse
        """
        age_list = ["1a4", "a1j", "1 3", "sfdjsdlkjflsd", " ", "  ", "   ", "^&*$@$@#", "a!#@*&!h", "*@&$u@$@#", "", "gjksdljgklsdgkld3kgjgkljklsdgkljsdfklgj"]
        for age in age_list:
            self.assertFalse(self.my_guest.validate_guest_age(age))
    def test_validate_guest_age_true(self):
        """
        A unittest to test the age of the guest.

        Test conducted:
        assertTrue
        """
        age_list = ["14", "1", "163", "27948293", "32", "323", "938", 5743, 213, 43, 0, 7348959832757934]
        for age in age_list:
            self.assertTrue(self.my_guest.validate_guest_age(age))