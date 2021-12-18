#!/usr/bin/env python
# coding: utf-8
import socket
import sys
import psutil
HELP_TEXT = """usage: python {program_name:s}
Displays the values of the sensors
Options and arguments:
--help:    Display this message"""
def ac_connected():
    """
    A function that checks to see if the power is connected 
    to the system. If it is, the function will return true.
    """
    ac_power = psutil.sensors_battery().power_plugged
    if ac_power is True:
        print("The ac adapter is connected.")
    else:
        print("The ac adapter is not connected.")
def command_line(argv):
    """
    A function that runs other user 
    defined functions inside of it.
    """
    #Try block
    try:
        program_name, *arguments = argv
        if not arguments:
            show_sensors()
        elif arguments and arguments[0] == '--help':
            print(HELP_TEXT.format(program_name=program_name))
            return
    except ValueError:
        print("Unknown arguments {}".format(arguments))
def cpu_load():
    """
    A function that checks the total amount of ram available 
    on the system and displays it within intercals of a tenth of a percent.
    """
    cpu_interval = psutil.cpu_percent(interval=0.1)
    print(cpu_interval)
def ip_addresses():
    """
    A function the gets the hostname, IP address 
    information, and appends everything to a list.
    """
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(socket.gethostname(), None)
    address_info = []
    for address in addresses:
        address_info.append((address[0].name, address[4][0]))
    return address_info
def python_version():
    """
    A function that checks the version of python you are running.
    """
    return sys.version_info
def ram_available():
    """
    A function that shows the user the 
    total amount of memory available on a system.
    """
    return psutil.virtual_memory().available
def show_sensors():
    """
    A function the displays the following:
        - cpu internval
        - Ram available
        - ac connection status
        - IP addresses
    """
    print("Python version: {0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        print(f"IP addresses: {address})")
    print(f"CPU Load: {cpu_load()}")
    print("RAM Available: {} MiB".format(ram_available() / 1024**2))
    print("AC Connected: {}".format(ac_connected()))
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
        #Printing out show_sensor_data.
        print(show_sensor_data)
        #Asking the user if they would like to record the data on an excel sheet.
        record_response = input("Would you like to record the data on a spreadsheet? Y/N")
        #Handling the case where the user enters y for yes.
        if record_response.lower() == "y":
            try:
                #Opening the csv file for writing.
                with open("sensor_data.csv","w") as sensor_data:
                    for line in show_sensor_data:
                        print(line)
            except:
                print("Sorry, but we can't do that at the moment.")
    #Handling the case where the user enters cl.
    elif user_choice.lower() == "cl":
        #Calling the command_line function
        cmd_line = command_line(sys.argv)

    #Handling the case where the user enters ac.
    elif user_choice.lower() == "ac":
        #Calling the ac_connected function.
        my_connection = ac_connected()
        #If the ac adapter is connected, do this.
        if my_connection == True:
            print("The adapter is connected.")
        #Starting a for loop.
        print(my_connection)
    #Handling the case where the user enters ac.
    elif user_choice.lower() == "vm":
        #Calling the ac_connected function.
        my_ram = ram_available()
        #Starting for loop.
        for ram in my_ram:
            #Printing out the contents.
            print(f"The system currently has {ram} ram available.")
    #Handling the case where the user enters e.
    elif user_choice.lower() == "e":
        #Try block.
        try:
            #Opening the csv file for writing.
            with open("sensor_data.csv","w") as sensor_data_csv:
                #For loop to run through the data.
                for data in ram:
                    #Writing each data entry to the file.
                    sensor_data_csv.write(data)
        #except block to handle the alternative case.
        except:
            print("Sorry, but we can't do that.")
        #Printing a message to the user.
        print("Now exiting the system....") 
        #Setting flag to true.
        not_done = True   
#ifmain construct.
if __name__ == '__main__':
    command_line(sys.argv)