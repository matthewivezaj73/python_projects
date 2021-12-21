#Importing libraries.
import numpy
#Importing the converter class.
from classes.converter import converter
#Creating an instance of the class.
my_converter = converter(98.33)
#Setting a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user to make a choice.
    user_choice = input("Please enter c to access the celsius fahrenheit calculator.")