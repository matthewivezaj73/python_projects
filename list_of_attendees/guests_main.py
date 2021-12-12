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
        my_guest.guest_name(add_person)
    #Creating a flag.
    not_age = False
    #Testing for adding a guest.
    while not not_age:
        #Asking for the user's input.
        add_age = input("What is the age of the guest?")
        #Validating the guest age
        my_guest.guest_age(add_age)
    #Creating a flag.
    not_phone = False
    #Testing for adding a guest phone number.
    while not not_phone:
        #Asking for the user's input.
        guest_phone = input("What is the phone number of the guest?")
        #Validating the guest phone.
        my_guest.guest_phone(guest_phone)
    #Creating a flag.
    not_type = False
    #Testing for adding a guest type.
    while not not_type:
        #Asking for the user's input.
        guestType = input("What is the type of guest?")
        #Validating the guest type.
        my_guest.guest_type(guestType)
    #Creating a list of the data gathered.
    guest_list = [add_person, add_age, guest_phone, guestType]
    #Created a variable and assigned it a file path.
    my_file = "text_files/guest_info.txt"
    #Opening a file for writing.
    with open(my_file) as txt_file:
        csv_file = "text_files/guest_info.csv"
        if os.isfile("text_files/guest_info.csv"): 
            #Creating the csv file.
            with open("text_files/guest_info.csv", "w+") as csv_file:
                for line in guest_list:
                    #Writing each guest info to the file.
                    csv_file.write(line)

