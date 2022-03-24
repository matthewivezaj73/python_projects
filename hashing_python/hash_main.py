#Importing the hashlib library.
import hashlib
#importing all methods from the hashes class.
from classes.hashes import *
#Creating an instance of the class.
my_hash = hashes("sha1","string",12)
#Created a flag.
not_done = False
#Testing for input.
while not not_done:
    print("here are all of the algorithm choices to choose from"+str(hashlib.algorithms_guaranteed))
    
    # #Adding a case.
    # if user_choice.lower() == "sha256":
    #     #Asking the individual for their name.
    #     your_phrase = input(b"Please enter your text here: ")
    #     #Assigning a sha256 hash to a variable.
    #     hashed_value = hashlib.sha256(your_phrase.encode())
    #     # creating a generic constructor
    #     generic = hashlib.new('sha256')
    #     #Printing the hashed value.
    #     print(f"Here is your name in a hashed value: {hashed_value}")
    # #handling the case where the user enters sha1.
    # elif user_choice.lower() == "sha1":
    #     #Asking the individual for their name.
    #     your_phrase = input(b"Please enter your text here: ")
    #     #Assigning a sha256 hash to a variable.
    #     hashed_value = hashlib.sha1(your_phrase.encode())
    #     # creating a generic constructor
    #     generic = hashlib.new('sha1')
    #     #Printing the hashed value.
    #     print(f"Here is your name in a hashed value: {hashed_value}")
    # #Handling the case where the user enters sha512.
    # elif user_choice.lower() == "sha512":
    #     #Asking the individual for their name.
    #     your_phrase = input(b"Please enter your text here: ")
    #     #Assigning a sha256 hash to a variable.
    #     hashed_value = hashlib.sha1(your_phrase.encode())
    #     # creating a generic constructor
    #     generic = hashlib.new('sha1')
    #     #Printing the hashed value.
    #     print(f"Here is your name in a hashed value: {hashed_value}")
    # #Handling the case where the user enters sha3_256.
    # elif user_choice.lower() == "sha3_256":
    #     #Asking the individual for their name.
    #     your_phrase = input(b"Please enter your text here: ")
    #     #Assigning a sha256 hash to a variable.
    #     hashed_value = hashlib.sha3_256(your_phrase.encode())
    #     # creating a generic constructor
    #     generic = hashlib.new('sha3_256')
    #     #Printing the hashed value.
    #     print(f"Here is your name in a hashed value: {hashed_value}")
    # #Handling the case where the user enters sha3_384.
    # elif user_choice.lower() == "sha3_384":
    #     #Asking the individual for their name.
    #     your_phrase = input(b"Please enter your text here: ")
    #     #Assigning a sha256 hash to a variable.
    #     hashed_value = hashlib.sha3_384(your_phrase.encode())
    #     # creating a generic constructor
    #     generic = hashlib.new('sha3_384')
    #     #Printing the hashed value.
    #     print(f"Here is your name in a hashed value: {hashed_value}")
    # #Handling the case where the user enters sha3_384.
    # elif user_choice.lower() == "shake_256":
    #     #Asking the individual for their name.
    #     your_phrase = input(b"Please enter your text here: ")
    #     #Assigning a sha256 hash to a variable.
    #     hashed_value = hashlib.shake_256(your_phrase.encode())
    #     # creating a generic constructor
    #     generic = hashlib.new('shake_256')
    #     #Printing the hashed value.
    #     print(f"Here is your name in a hashed value: {hashed_value}")

        