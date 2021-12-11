#Importing module.
from classes.validation import *
#Importing a library.
import argparse
import os
import subprocess
#Making a flag.
not_done = False
#Creating a list
protocolList = []
#Creating a parser
parser = argparse.ArgumentParser(description = "")
#Adding arguments to the parser.
parser.add_argument("-p1", dest="param1", help="parameter1")
#Creating an instance of the class.
validator = Validate("SMTP", 32)
#Creating a list.
protocolListValues = []
#Testing for user input.
while not not_done:
    #Giving the user choices.
    print("Please enter a to add protocols in use.\nPlease enter s to show the ports protocols run on.\nPlease enter r to run a DOS o PowerShell command\nPlease enter e to exit the program.\nPlease make your choice: ")
    #Accepting user input.
    user_choice = input("")
    #Handling the case where the user selects a.
    if user_choice.lower() == "a":
        #Inserting a action.
        protocolList.append("TLS")
        #Adding a value for TLS
        tls_value = 443
        #Appending the tls_value
        protocolListValues.append(tls_value)
        #Inserting a action.
        protocolList.append("SSL")
        #Adding a value for ssl
        ssl_value = 443
        #Appending the ssl_value
        protocolListValues.append(ssl_value)
        #Inserting a action.
        protocolList.append("sftp")
        #Adding a value for sftp
        sftp_value = 443
        #Appending the sftp_value
        protocolListValues.append(sftp_value)
        #Inserting a action.
        protocolList.append("https")
        #Adding a value for https
        https_value = 443
        #Assigning 0 to x.

        ############################################ ADDING NEW SECURITY PROTOCOLS ############################################
        #Inserting a protocol.
        protocolList.append("IPSec")
        #Inserting a protocol.
        protocolList.append("kerberos")
        #Inserting a protocol.
        protocolList.append("SSH")
        #Inserting a protocol.
        protocolList.append("SMTP")
        #Assigning the port number to smtp.
        smtp_value = 443
        #Inserting the port number for SMTP.
        protocolListValues.append(smtp_value)
        #Inserting a protocol.
        protocolList.append("HTTP")
        #Inserting a protocol.
        protocolList.append("SFTP")
        #Inserting a protocol.
        protocolList.append("OSPF")
        #Inserting a protocol.
        protocolList.append("PCT")
        #Inserting a protocol.
        protocolList.append("ZRTP")
        #Inserting a protocol.
        protocolList.append("PGP")
        









        x = 0
        #Creating a dictionary 
        my_dict = {protocolList[0]:tls_value,protocolList[1]:ssl_value,protocolList[2]:sftp_value,protocolList[3]:https_value}
        #setting a flag.
        add_more = False
        #Testing for adding more data.
        while not add_more:
            #Setting a flag.
            not_add_key = False
            #Printing out the protocols to choose from.
            for proto in protocolList:
                print(proto)
            #Gathering user input.
            while not not_add_key:
                #Asking the user for a protocol to use.
                config_key = input("Please enter a security protocol category you would like to use: ")
                #Validating the key.
                not_add_key = validator.validate_Key(config_key)
            #Setting a flag.
            not_add_value = False
            #Gathering user input.
            while not not_add_value:
                #Asking the user for a protocol to use.
                config_value = input("Please enter a security protocol value you would like to use: ")
                #Validating the variable.
                not_add_value = validator.validate_Value(config_value)
            #Adding new data to the dictionary
            new_dict = {config_key:config_value} 
            #Appending the key to the list.
            protocolList.append(config_key)           
            #Updating the original dictionary with the new values the user entered.
            my_dict.update(new_dict)
            #Assigning the file name to a variable.
            my_file = "text_files/keys_in_use"
            if os.path.isfile(my_file):
                with open("keys_in_use.txt","w") as txt_file:
                    for line in txt_file:
                        txt_file.write(line)
            else:    
                with open("keys_in_use.txt","w+") as txt_file:
                    for line in txt_file:
                        txt_file.write(line)
            add_more = True
        #Printing out the list.
        for protocol in protocolList:
            #Counting the number of protocols.
            print(f"there is {str(protocolList.count(protocol))} protocols in use by the name of:") 
            #Printing a message with each protocol.
            print(f"{protocol} in use...")
    #Handling the case where the user enters s.
    elif user_choice.lower() == "s":
        #Start of try block
        try:
            #For loop to print everything in the dictionary in a formated way.
            for key,value in my_dict.items():
                print(f"The service is {key} and it is running on port {value}")
        #Handling the case where the user is unable to show the protocols.
        except:
            print("You need to select option a to add protocols before you can do that!")
    #Handingling the case where the user enters r.
    elif user_choice.lower() == "r":
        #Start of try/except
        # try:
        #     with open("text_files/cmd_output.txt") as txt_file:
        #Accepting user input.
        user_selection = input("Please input a cmd command you would like to run and print contents out to a csv file: ")
        #Handling the case where a user enters net.
        if user_selection.lower() == "net":
################## THIS SECTION STILL NEEDS WORK ##################
            #Running the net cmd command and assigning it to a variable.
            net_content = subprocess.run(["net"])

            #Assigning the file path to a variable
            file = "text_files/cmd_output.csv"
#################################### PROBLEM LIES HERE ####################################
            if os.path.isfile("text_files/cmd_output.txt"):
                #Opening a file.
######################################PROBLEM WITH AREA IS                
                with open("text_files/cmd_output.txt", "w") as this_text_file:
                    (this_text_file.write(subprocess.run(["net"])))
                    # with open("text_files/cmd_output.txt","w") as txt_file:
                        
#################################### PROBLEM IS ABOVE  ####################################
                            # txt_file.write(line)
                            
                            
                    #Checking if the file exists.
                    if os.path.isfile(file):
                        #Opening the file for writing.
                        with open(file, "w") as csv_file:
                            
                            #For loop to write each line to the csv file.
                            for line in net_content:
                                #Writing each line to the file.
                                print(line)#csv_file.write(line)
                                
                    #handling the case where the file does not exist.
                    else:
                        #Creating the file if it does not exist and writing to it.
                        with open(file, "w+") as new_csv_file:
                            #A for loop to write each line to the file.
                            for line in net_content:
                                #Writing each line to the new file.
                                print(line)#new_csv_file.write(line)

            else:
                #Opening a file.
                with open("text_files/cmd_output.txt", "w+") as txt_file:
                    with open("text_files/cmd_output.txt","w") as txt_file:
#################################### PROBLEM IS ABOVE  ####################################
                        txt_file.write(line)
                    #Checking if the file exists.
                    if os.path.isfile(file):
                        #Opening the file for writing.
                        with open(file, "w") as csv_file:
                            
                            #For loop to write each line to the csv file.
                            for line in net_content:
                                #Writing each line to the file.
                                print(line)#csv_file.write(line)
                                
                    #handling the case where the file does not exist.
                    else:
                        #Creating the file if it does not exist and writing to it.
                        with open(file, "w+") as new_csv_file:
                            #A for loop to write each line to the file.
                            for line in net_content:
                                #Writing each line to the new file.
                                print(line)#new_csv_file.write(line)
################## THIS SECTION STILL NEEDS WORK ##################
            #Handling the case where a user enters cls.
        elif user_selection.lower() == "cls":
            #Running the cls cmd command.
            subprocess.run(["cls"])
        # except:
        #     print(f"I am sorry, but {user_selection} cannot be ran at this time\nThere may be another command that must be run before\nthis one can be ran.")
        #End of try/except
    #Handling the case where the user enters e.
    elif user_choice.lower() == "e":
        #Notifying the user that you are exiting the program.
        print("Now exiting the program...")
        #Setting flag to true to break out of the loop.
        not_done = True