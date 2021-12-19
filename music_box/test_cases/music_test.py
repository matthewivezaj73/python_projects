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
        self.new_music = ValidateMusic("Mike L", "Omega", "Sprigal")
    def test_validate_album_false(self):
        """
        A method that will ensure that validate_album returns false.
        """
        invalid_artist_list = ["R0cky!", "!R0cky", "R0*cky!", "#R0cky!", " Rocky", "Rocky "," Rocky ", " ", "   ","&*@*$&#$","%","%*","1_2","                 "]
        for artist in invalid_artist_list:
            self.new_music.validate_album(artist)
    def test_validate_album_true(self):
        """
        A method that will ensure that validate_album returns true.
        """
        invalid_artist_list = ["R0cky","Monty", "1Monty", "Monty3","A$AP R0CKY","Monty$","$Monty","$Monty$"]
        for artist in invalid_artist_list:
            self.new_music.validate_album(artist)

    def test_validate_artist_false(self):
        """
        A method that will ensure that validate_artist returns false.
        """
        invalid_artist_list = ["R0cky!", "!R0cky", "R0*cky!", "#R0cky!", " Rocky", "Rocky "," Rocky ", " ", "   ","&*@*$&#$","%","%*","1_2","                 "]
        for artist in invalid_artist_list:
            self.new_music.validate_artist(artist)
    def test_validate_artist_true(self):
        """
        A method that will ensure that validate_artist returns true.
        """
        invalid_artist_list = ["R0cky","Monty", "1Monty", "Monty3","A$AP R0CKY","Monty$","$Monty","$Monty$"]
        for artist in invalid_artist_list:
            self.new_music.validate_artist(artist)
