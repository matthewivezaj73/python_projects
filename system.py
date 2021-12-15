#Importing the socket module.
import socket
#Creating a flag.
not_host = False
#Testing for user input.
while not not_host:
    #Assigning a variable to the hostname.
    hostname = socket.gethostname()