#Importing the socket, psutil libraries.
import socket
import psutil
#Creating a flag.
not_host = False
#Creating a list to hold a bunch of dictionaries.
user_info = []
#Testing for user input.
while not not_host:
    #Asking the user to make a choice.
    user_choice = input("Please enter \'h\' if you would like to check the file directory this program is running from.\nPlease enter \'a\' if you would like to check the ip address of the system.\nPlease enter \'s\' if you would like to check cpu stats.\nPlease enter \'p\' if you would like to check the cpu percent.")
    #Try block
    try:
        #handling the case where the user selects option h.
        if user_choice.lower() == "h":
            #Assigning a variable to the hostname.
            hostname = socket.gethostname()
            #Printing the hostname
            print(hostname)
        #Handling the case where the user selects option a.
        elif user_choice.lower() == "a":
            #Grabbing the ip address of the system and assigning it to a variable.
            ipaddress = socket.getaddrinfo(hostname,None)
            #Printing the ipaddress.
            print(ipaddress)
        #Handling the case where the user selects option s.
        elif user_choice.lower() == "s":
            #Grabbing the cpu stats and assigning them to a variable.
            cpustats = psutil.cpu_stats()
            #Printing the cpu stats.
            print(cpustats)
        #Handling the case where the user selects option p.
        elif user_choice.lower() == "p":
            #Assigning the cpu percentage to a variable.
            cpupercent = psutil.cpu_percent(interval=0.1)
            #Printing the cpu percentage.
            print(cpupercent)
    #Handling the case where the cases above are not met.
    except:
        print("You must first grab the host name by entering \'h\'")

