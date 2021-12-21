#Importing libraries.
import numpy as num
#Importing module.
from classes.converter import converter
#Setting a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user what they would like to do.
    user_choice = input("Please enter cf if you would like to convert Celsius to Fahrenheit.")
    #Handing the case if the user selects cf.
    if user_choice.lower() == "cf":
        celsius_to_fahrenheit(numpy.identity(3))