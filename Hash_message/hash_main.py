#Setting a flag.
from hashlib import sha256


not_done = False
#Testing for user input.
while not not_done:
    #Asking the user what they would like to do.
    user_choice = input("Please enter the type of encryption you would like to encrypt your message in: ")
    #Handling the case where the user enters sha256.
    if user_choice.lower() == "sha256":
        #Asking the user to input a phrase.
        user_phrase = input("Please enter a phrase to encrypt: ")
        #Turning the phrase into unicode.
        #Assigning the encrypted message to a variable.
        your_choice = sha256(user_phrase)
        #Printing the message.
        print(your_choice)