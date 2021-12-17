#!/usr/bin/env python
# coding: utf-8
import socket
import sys
import psutil
HELP_TEXT = """usage: python {program_name:s}
Displays the values of the sensors
Options and arguments:
--help:    Display this message"""
def python_version():
    """
    A function that checks the version of python you are running.
    """
    return sys.version_info
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
def cpu_load():
    """
    A function that checks the total amount of ram available 
    on the system and displays it within intercals of a tenth of a percent.
    """
    return psutil.cpu_percent(interval=0.1)
def ram_available():
    """
    A function that shows the user the 
    total amount of memory available on a system.
    """
    return psutil.virtual_memory().available
def ac_connected():
    """
    A function that checks to see if the power is connected 
    to the system. If it is, the function will return true.
    """
    return psutil.sensors_battery().power_plugged
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
    #End of try block
#Setting a flag.
not_done = False
#Testing for input.
while not not_done:
    #Asking the user to enter in a choice.
    user_choice = input("Please enter one of the following choices:\n\n    - Please enter \'ss\' to show the sensor information.\n\n"+
    "    - Please enter \'cl\' to show the command line.\n\n    - Please enter \'e\' to exit the program.\n\n")
    #Handling the case where the user enters ss.
    if user_choice.lower() == "ss":
        #Calling the show sensors function
        show_sensors()
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
#ifmain construct.
if __name__ == '__main__':
    print()