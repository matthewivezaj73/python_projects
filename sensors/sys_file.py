#!/usr/bin/env python
# coding: utf-8
from classes.sys_functions import *
#Setting a flag.
not_done = False
#Testing for input.
while not not_done:
    #Asking the user to enter in a choice.
    user_choice = input("Please enter one of the following choices:\n\n    - Please enter \'ss\' to show the sensor information.\n\n"+
    "    - Please enter \'cl\' to show the command line.\n\n    - Please enter \'e\' to exit the program.\n\n"+
    "   - Please enter \'ac\' to show the adapter connection status.\n\n   - Please enter \'vm\' to show the virtual memory available.")
    #Handling the case where the user enters ss.
    if user_choice.lower() == "ss":
        #Calling the show sensors function
        show_sensor_data = show_sensors()
        print(show_sensor_data)            
    #Handling the case where the user enters cl.
    elif user_choice.lower() == "cl":
        #Calling the command_line function
        cmd_line = command_line(sys.argv)
        if cmd_line == None:
            print("The AC Adapter is not connected.")
        #Handling the case where the cmd_line is not none.
        else:
            print (cmd_line)
    #Handling the case where the user enters ac.
    elif user_choice.lower() == "ac":
        #Calling the ac_connected function.
        ac_connected()
        #If the ac adapter is connected, do this.
        # if my_connection == True:
        #     print("The adapter is connected.")
        # #Handling the alternative case.
        # elif my_connection == None:
        #     print("The adapter is not connected.")
        # #Handling the last case where something wrong happened.
        # else:
        #     print("Something wrong happened.")
    #Handling the case where the user enters ac.
    elif user_choice.lower() == "vm":
        #Calling the ac_connected function.
        my_ram = ram_available()
        #Printing out a formated string.
        print(f"The system currently has {my_ram} ram available.")
    #Handling the case where the user enters e.
    elif user_choice.lower() == "e":
        #Try block.
        # try:
        #Opening the csv file for writing.
        with open("sensor_data.csv","w") as sensor_data_csv:
            #Writing each data entry to the file.
            sensor_data_csv.write(str(my_ram))
        # #except block to handle the alternative case.
        # except:
        #     print("Sorry, but we can't do that.")
        #Printing a message to the user.
        print("Now exiting the system....") 
        #Setting flag to true.
        not_done = True   
#ifmain construct.
if __name__ == '__main__':
    command_line(sys.argv)