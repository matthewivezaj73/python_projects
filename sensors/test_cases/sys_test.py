#Importing the unittest module.
import unittest
#Importing the Guests module.
from functions.sys_functions import *
#Creating the class.
class TestCrypto(unittest.TestCase):
    """
    A representation of test cases written 
    to evaluate the method in a program.
    """
    def test_sys_ac_connected_assertEqual(self):
        """
        A test to see if the ac_connected function will evaluate to itself.

        Test used: assertEqual.
        """
        

        self.assertEqual(ac_connected(),ac_connected())
    def test_sys_ac_connected_assert_assertNotEqual(self):
        """
        A test to see if the ac_connected function will evaluate to Not Equal.

        Test used: assertNotEqual.
        """
        self.assertNotEqual(ac_connected(), "5")
    def test_sys_command_line_assert_NotIn(self):
        """
        A test to see if the ac_connected function will 
        
        assert a value is can not be run inside of it.

        Test used: assertIn.
        """
        
        self.assertEqual(command_line("12"),command_line("jh325432"))
    def test_sys_command_line_assert_In(self):
        """
        A test to see if the ac_connected function will evaluate to true.

        Test used: assertNotIn.
        """
        self.assertNotEqual(command_line("12"), "command_line()")