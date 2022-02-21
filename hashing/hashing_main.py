#Importing libraries.
import hashlib
#Setting a flag.
not_done = False

# BEGUN THE STEP WHERE I COLLECT INPUT FROM THE USER.

#Testing for user input.
while not not_done:
    #Asking the user for iput.
    input_text = input("Please enter a phrase you would like hashed: ")
    #Hashing the text.
    hashed_text = hash(input_text)
    #Typecasting the hashed text.
    hashed_text = str(hashed_text)
    #Printing the hashed value.
    print(hashed_text)


# END THE STEP WHERE I COLLECT INPUT FROM THE USER.