#Importing the hashlib library.
import hashlib
#Created a flag.
not_done = False
#Testing for input.
while not not_done:
    print("here are all of the algorithm choices to choose from"+str(hashlib.algorithms_guaranteed))
    #Asking the user for their choice of encoding.
    user_choice = input("Please enter the type of encoding you would like to encode your string in: ")
    #Adding a case.
    if user_choice.lower() == "sha256":
        #Asking the individual for their name.
        your_phrase = input(b"Please enter your text here: ")
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.sha256(your_phrase.encode())
        # creating a generic constructor
        generic = hashlib.new('sha256')
        #Printing the hashed value.
        print(f"Here is your name in a hashed value: {hashed_value}")
        
    elif user_choice.lower() == "sha1":
        #Asking the individual for their name.
        your_phrase = input(b"Please enter your text here: ")
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.sha1(your_phrase.encode())
        # creating a generic constructor
        generic = hashlib.new('sha1')
        #Printing the hashed value.
        print(f"Here is your name in a hashed value: {hashed_value}")
    #Handling the case where the user enters sha512.
    elif user_choice.lower() == "sha512":
        #Asking the individual for their name.
        your_phrase = input(b"Please enter your text here: ")
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.sha1(your_phrase.encode())
        # creating a generic constructor
        generic = hashlib.new('sha1')
        #Printing the hashed value.
        print(f"Here is your name in a hashed value: {hashed_value}")