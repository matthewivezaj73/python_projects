#https://github.com/matthewivezaj73/python_projects/tree/main/list_of_attendees
#Importing the validate_guests file and the Guests class.
from classes.validate_guests import Guests
#Importing the os library.
import os
#Creating an instance of the class.
my_guest = Guests("Sally", 22, 8374734624, "Guest")
#Adding a flag
not_guest = False
#testing for guests.
while not not_guest:
    #Creating a flag.
    not_add = False
    #Testing for adding a guest.
    while not not_add:
        #Asking for the user's input.
        add_person = input("What is the name of the guest?")
        #Validating the guest name
        not_add = my_guest.validate_guest_name(add_person)
    #Creating a flag.
    not_age = False
    #Testing for adding a guest.
    while not not_age:
        #Asking for the user's input.
        add_age = input("What is the age of the guest?")
        #Validating the guest age
        not_age = my_guest.validate_guest_age(add_age)
    #Creating a flag.
    not_phone = False
    #Testing for adding a guest phone number.
    while not not_phone:
        #Asking for the user's input.
        guest_phone = input("What is the phone number of the guest?")
        #Validating the guest phone.
        not_phone = my_guest.validate_guest_phone(guest_phone)
    #Creating a flag.
    not_type = False
    #Testing for adding a guest type.
    while not not_type:
        #Asking for the user's input.
        guestType = input("What is the type of guest?")
        #Validating the guest type.
        not_type = my_guest.validate_guest_type(guestType)
    #Creating a list of the data gathered.
    guest_list = [add_person, add_age, guest_phone, guestType]
    #Created a variable and assigned it a file path.
    my_file = "text_files/guest_info.txt"
    if os.path.isfile(my_file):
        #Opening a file for writing.
        with open(my_file) as txt_file:
            #Assigning the file path to a variable.
            csv_file = "text_files/guest_info.csv"
            #Checking if the csv file exists.
            if os.path.isfile("text_files/guest_info.csv"): 
                #Creating the csv file.
                with open("text_files/guest_info.csv", "a") as csv_file:
                    for line in guest_list:
                        guest_len = len(guest_list)
                        # print(guest_len)
                        #Writing each guest info to the file.
                        csv_file.write(line)
                        csv_file.write(",")
                        if guest_len:
                            csv_file.write("\n")

    else:
        #Opening a file for writing.
        with open(my_file, "w+") as txt_file:
            #Assigning the file path to a variable.
            csv_file = "text_files/guest_info.csv"
            #Checking if the csv file exists.
            if os.path.isfile("text_files/guest_info.csv"): 
                #Creating the csv file.
                with open("text_files/guest_info.csv", "w+") as csv_file:
                    for line in guest_list:
                        guest_len = len(guest_list)
                        # print(guest_len)
                        #Writing each guest info to the file.
                        csv_file.write(line)
                        csv_file.write(",")
                        if guest_len:
                            csv_file.write("\n")
            #Handling the alternative case.
            else: 
                #Creating the csv file.
                with open("text_files/guest_info.csv", "a") as csv_file:
                    for line in guest_list:
                        guest_len = len(guest_list)
                        # print(guest_len)
                        #Writing each guest info to the file.
                        csv_file.write(line)
                        csv_file.write(",")
                        if guest_len:
                            csv_file.write("\n")
        #Setting flag to false.
        not_question = False
        #Testing for the user input.
        while not_question:
            #Asking for user input.
            exit_now = input("Would you like to stop adding guests? Y/N: ")
            #If the user enters y for yes.
            if exit_now.lower() == "y":
                #Setting flags to exit the loop
                not_guest = True
                not_question = True
            #If the user enters n for no.
            elif exit_now.lower() == "n":
                #Setting flags to exit the loop
                not_guest = False
                not_question = True
            #Handling all other cases.
            else:
                print(f"Sorry, I did not understand{exit_now}, please try again!")