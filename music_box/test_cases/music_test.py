#Importing the unittest module.
import unittest
#Importing the Guests module.
from classes.validate_music_box import ValidateMusic
#Creating the class.
class TestMusic(unittest.TestCase):
    def __init__(self):
        """
        Creating an instance of the Validate Music class.
        """
        #Creating an instance of the class.
        new_music = ValidateMusic("Mike L", "Omega", "Sprigal")
    def test_validate_artist_false(self):
        """
        
        """
