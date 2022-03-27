#Importing from a folder.
from classes.hashing_methods import Hashing
#Setting a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Requesting user input.
    user_choice = input("Enter an algorithm to generate a string and encrypt it in that algorithm: ")
    #Handling the case where the user selects SHA256.
    if user_choice.lower() == "sha256":
        