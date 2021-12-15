#Importing the socket module.
import socket
#Creating a flag.
not_host = False
#Testing for user input.
while not not_host:
    #Asking the user to make a choice.
    user_choice = input("Please enter h if you would like to check the file directory this program is running from.\n")
    #handling the case where the user selects option h.
    if user_choice.lower() == "h":
        #Assigning a variable to the hostname.
        hostname = socket.gethostname()
