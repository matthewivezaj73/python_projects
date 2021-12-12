import unittest
#Import all methods from InventoryItem in the classes folder.
from classes.validation import Validate
class TestCrypto(unittest.TestCase):
    """
    Creating a class for unittesting.
    """
    def setUp(self):
        """
        Create an instance of the Vehicle class for testing all class functions.
        """
        #Creating an instance of the Vehicle class.
        self.new_validator = Validate("GPG","43")
    def test_validate_key_assert_False(self):
        """
        Checks to ensure that the chars in the character 
        list can indeed not be passed in the individual_name_check method.

        Method ran:
        individual_name_check

        Test ran: 
        AssertFalse
        """
        #Creating a list of improper names.
        list_of_improper_names = ["!Frank","Frank!","@Fra(nk!","&*@($*#@&$*#@","1frank","frank2","1fra2nk4","1fra@nk1","47482374239",""," "]
        #Looping through each value in the list.
        for name in list_of_improper_names:
            self.assertFalse(self.new_vehicle.individual_name_check(name))
    def test_validate_key_assert_True(self):
        """
        Checks to ensure that the chars in the character 
        list can indeed be passed in the validate_Key method.

        Method ran:
        validate_Key

        Test ran: 
        AssertTrue
        """
        #Creating a list of proper names.
        list_of_proper_names = ["IPSec", "SSL", "TLS", "kerberos", "SSH", "SMTP", "HTTP", "HTTPS", "SFTP", "OSPF", "PCT", "ZRTP", "PGP"] 
        #Looping through each name in the list.
        for name in list_of_proper_names:
            self.assertTrue(self.new_validator.validate_Key(name))
    def test_validate_value_check_Assert_False(self):
        """
        Testing to see if the chars are only comprised of digits and a period
        so that they may indeed not be passed by the pricvalidate_valuee_paid method.

        Method ran:
        validate_value

        Test ran:
        assertFalse
        """
        #Creating a list of bad values.
        value_list = ["1IPSec", "Peanuts", "TS", "k53beros5", "1SSH4", "#5434", "2432(", "@HTTPS5", "", " ", "  ", "Z247982374329Tjgfsadjfas;lflkjdsakfjkdsajfsaP"]
        #Checking to see if the items in the list will fail the check.
        for value in value_list:
            self.assertFalse(self.new_validator.validate_Value(value))
    def test_validate_value_Assert_True(self):
        """
        Testing to see if the chars are only comprised of digits and a period
        so that they may indeed be passed by the validate_value method.

        Method ran:
        validate_value

        Test ran:
        assertTrue
        """
        #Creating a list of of good values.
        value_list = [2221,2221,23,11111,11,18748392,2112,211,114,141]
        #Testing to see if the price will pass the price check.
        for value in value_list:
            self.assertTrue(self.new_validator.validate_Value(value))
