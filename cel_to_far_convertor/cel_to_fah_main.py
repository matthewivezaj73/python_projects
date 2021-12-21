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
    user_choice = input("Please enter \'cf\' if you would like to convert Celsius to Fahrenheit.\n\nPlease enter \'kc\' if you would like to convert Celsius to kelvin.\n\nPlease enter \'e\' if you would like to exit the program: ")
    #Handling the case where the user enters cf.
    if user_choice.lower() == "cf":
        #Setting a flag.
        not_cf = False
        #Testing for input.
        while not not_cf:
            #Asking for user on what degree celsius they would like to input.
            degree_celsius = input("Please enter the degrees celsius: ")
            #Calling the celcius_fahrenheit_converter method.
            not_cf = my_converter.celcius_fahrenheit_converter(degree_celsius)
    elif user_choice.choice.lower() == "kc":
        #Setting a flag.
        not_kv = False
        #Testing for input.
        while not not_kv:
            #Asking for user on what degree kelvin they would like to input.
            degree_celsius_kelvin = input("Please enter the degrees celsius: ")
            #Calling the celsius_kelvin_converter method.
            not_cf = my_converter.celsius_kelvin_converter(degree_celsius_kelvin)
    #Handling the case where the user selects e to exit.
    elif user_choice.choice.lower() == "e":
        #Setting a flag.
        not_done = False
    #Handling the alternative case.
    else:
        print(f"Sorry, I did not understand \'{user_choice}\', please try again.")