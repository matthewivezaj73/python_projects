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
    print(ac_power)
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
    "    - Please enter \'cl\' to show the command line.\n\n    - Please enter \'e\' to exit the program.\n\n   - Please enter \'ac\' to show the adapter connection status.\n\n   - Please enter \'vm\' to show the virtual memory available.")
    #Handling the case where the user enters ss.
    if user_choice.lower() == "ss":
        #Calling the show sensors function
        show_sensors()
        #Asking the user if they would like to record the data on an excel sheet.
        record_response = input("Would you like to record the data on a spreadsheet? Y/N")
        #Handling the case where the user enters y for yes.
        if record_response.lower() == "y":
            
    #Handling the case where the user enters cl.
    elif user_choice.lower() == "cl":
        #Calling the command_line function
        command_line(sys.argv)
    #Handling the case where the user enters e.
    elif user_choice.lower() == "e":
        #Setting flag to true.
        not_done = True
        #Printing a message to the user.
        print("Now exiting the system....")    
    #Handling the case where the user enters ac.
    elif user_choice.lower() == "ac":
        #Calling the ac_connected function.
        ac_connected()
#ifmain construct.
if __name__ == '__main__':
    command_line(sys.argv)