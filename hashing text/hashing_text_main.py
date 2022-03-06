#Importing a class file.
from classes.hash_me import *
#Creating a flag.
not_done = False
#Testing for the users input.
while not not_done:
    #Asking the user what they would like to do.
    user_input = input("Enter \'S\' \n\n**(without single quotes)** \n\nif you would like to add a string to be hashed.")

    if user_input.upper() == 'S':
        
        my_text = hash(inputted_text)
        print(my_text)
