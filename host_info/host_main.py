#Import libraries
import socket
import psutil
#Creating a blank list.
#Creating a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user for a choice.
    user_choice = input("Please enter a if you would like to add a configuration.")
    #Handling the case where the user enters a.
    if user_choice.lower() == "a":
