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
    def setUp(self):
        
    def test_sys_ac_connected_assert_False(self):
        """
        A test to see if the ac_connected function will evaluate to false.

        Test used: assert false.
        """
