#Importing from a folder.
from classes.hashing_methods import Hashing
#Setting a flag.
not_done = False
#Instantiating the class.
my_hash = Hashing("Hello sir","SHA-256",64)
#Testing for user input.
while not not_done:
    #Requesting user input.
    user_choice = input("Enter an algorithm to generate a string and encrypt it in that algorithm: ")
    #Handling the case where the user selects SHA256.
    if user_choice.lower() == "sha256":
        #asking the user to input a message
        my_message = input("Please enter a message you would like encrypted.")
        #Calling the sha256 method to encrypt the message.