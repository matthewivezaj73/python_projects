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
    user_input = input("Enter \'S\' \n**(without single quotes)** \nif you would like to add a string to be hashed.\nEnter \'R\' \n**(without single quotes)** \nif you would like to show what is inside of the list.")

    if user_input.upper() == 'S':
        #Setting a flag to false.
        not_hashed = False
        #Testing for the hashed input.
        while not not_hashed:
            #Asking the user to enter a phrase.
            raw_text = input("Please enter a phrase you would like hashed: ")
            #Verifying that the input is greater than 0.
            greater_than_one = my_hash.get_text(raw_text)
            #Checking if the text has characters in it.
            if greater_than_one == True:
                #Hashing the text.
                hashed_text = hash(raw_text)
                #Printing the hashed text out.
                print(hashed_text)
                #Creating a dictionary and appending it to a list.
                hashed_list.append({"Hashed value:":hashed_text})
                #Verifying that the input is greater than 0.
                not_hashed = my_hash.get_text(raw_text)
            else:
                print(f"\'{raw_text}\' is not greater than zero, please try again!")
    #Handling the case where the user selects R.
    elif user_input.upper() == "R":
        print(hashed_list)
