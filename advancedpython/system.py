#Importing the socket module.
import socket
#Creating a flag.
not_host = False
#Creating a list to hold a bunch of dictionaries.
user_info = []
#Testing for user input.
while not not_host:
    #Asking the user to make a choice.
    user_choice = input("Please enter \'h\' if you would like to check the file directory this program is running from.\nPlease enter \'a\' if you would like to check the ip address of the system.\n")
    #handling the case where the user selects option h.
    if user_choice.lower() == "h":
        #Assigning a variable to the hostname.
        hostname = socket.gethostname()
    #Handling the case where the user selects option a.
    elif user_choice.lower() == "a":
        #Grabbing the ip address of the system and assigning it to a variable.
        ipaddress = socket.getaddrinfo(hostname)


