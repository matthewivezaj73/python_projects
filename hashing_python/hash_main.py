#Importing the hashlib library.
import hashlib
#Created a flag.
not_done = False
#Testing for input.
while not not_done:
    user_choice = input("Please enter the type of encoding you would like to encode your string in: ")
    #Asking the individual for their name.
    your_name = input("Please enter your name here: ")
    #Assigning a sha256 hash to a variable.
    hashed_value = hashlib.sha256(your_name.encode())
    # creating a generic constructor
    generic = hashlib.new('sha256')
    print(f"Here is your name in a hashed value: {hashed_value}")
