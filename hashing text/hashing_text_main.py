#Importing a class file.
from classes.hash_me import *
#Creating a class instance.
my_hash = Hashing("Hello")
#Creating a blank list.
hashed_list = []
#Creating a flag.
not_done = False
#Testing for the users input.
while not not_done:
    #Asking the user what they would like to do.
    user_input = input("Enter \'S\' \n\n**(without single quotes)** \n\nif you would like to add a string to be hashed.")

    if user_input.upper() == 'S':
        #Setting a flag to false.
        not_hashed = False
        #Testing for the hashed input.
        while not not_hashed:
            #Asking the user to enter a phrase.
            raw_text = input("Please enter a phrase you would like hashed: ")
            #Hashing the text.
            hashed_text = hash(raw_text)
            #Printing the hashed text out.
            print(hashed_text)
