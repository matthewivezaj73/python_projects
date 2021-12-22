#Importing the unittest module.
import unittest
#Importing the Guests module.
from functions.sys_functions import *
#Creating the class.
class TestCrypto(unittest.TestCase):
    """
    A representation of test cases written 
    to evaluate the functions in a program.
    """
    def test_sys_ac_connected_assert_False(self):
        """
        A test to see if the ac_connected function will evaluate to false.

        Test used: assert false.
        """
        self.assertFalse(ac_connected())
    def test_sys_ac_connected_assert_True(self):
        """
        A test to see if the ac_connected function will evaluate to true.

        Test used: assert true.
        """
        self.assertTrue(ac_connected())