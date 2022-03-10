#Setting a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user what they would like to do.
    user_choice = input("Please enter the type of encryption you would like to encrypt your message in: ")
    if user_choice.lower() == "sha256":
        