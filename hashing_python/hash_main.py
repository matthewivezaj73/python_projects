#Importing the hashlib library.
import hashlib
#Created a flag.
not_done = False
#Testing for input.
while not not_done:
    #Asking the user for their choice of encoding.
    user_choice = input("Please enter the type of encoding you would like to encode your string in: ")
    #Adding a case.
    if user_choice.lower() == "sha256":
        #Asking the individual for their name.
        your_name = input(b"Please enter your text here: ")
        #Assigning a sha256 hash to a variable.
        hashed_value = hashlib.sha256(your_name.encode())
        # creating a generic constructor
        generic = hashlib.new('sha256')
        print(f"Here is your name in a hashed value: {hashed_value}")
