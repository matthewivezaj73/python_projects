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
        A test to see if the ac_connected function will evaluate to it's opposite.

        Test used: assertEqual.
        """
        ac_power = not ac_connected()
        if ac_power == True:
            self.assertNotEqual(ac_connected(),ac_power)
    def test_sys_ac_connected_assert_True(self):
        """
        A test to see if the ac_connected function will evaluate to true.

        Test used: assert true.
        """
        self.assertTrue(ac_connected())
    def test_sys_command_line_assert_NotIn(self):
        """
        A test to see if the ac_connected function will 
        
        assert a value is can not be run inside of it.

        Test used: assertIn.
        """
        argv_list = ["12", "afd", "Ajs", "AJS", "dsad123", "FSD76", "HJjh234","2sd4","g231h","G342J","1HJK6"]
        for arg in argv_list:
            self.assertNotIn(command_line(arg))
    def test_sys_command_line_assert_In(self):
        """
        A test to see if the ac_connected function will evaluate to true.

        Test used: assertNotIn.
        """
        self.assertIn(command_line())