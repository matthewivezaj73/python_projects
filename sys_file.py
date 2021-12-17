#!/usr/bin/env python
# coding: utf-8

#The first line defines the interpreter 
# and the second line defines the encoding for the project.

#Importing the following libraries:
# - socket
# - sys
# - psutil
import socket
import sys
import psutil
#Assigning help text to a variable.
HELP_TEXT = """usage: python {program_name:s}
Displays the values of the sensors
Options and arguments:
--help:    Display this message"""
################## ---------------------- Begin adding functions. ---------------------- ##################
def check_power():
    """
    A function that checks to 
    see if the power is connected on a system.

    Function used:
    - sensors_battery
    """
    return psutil.sensors_battery().power_plugged
def command_line(argv):
    """
    A function that brings up a command line to the user.
    """
    #Starting a try block.
    try:
        program_name, *arguments = sys.argv
        if not arguments:
            show_sensors()
        elif arguments and arguments[0] == '--help':
            print(HELP_TEXT.format(program_name=program_name))
            return
        else:
            print("Sorry, we can't do that.")
    except ValueError:
        print("Unknown arguments {}".format(arguments))
def get_ram():
    """
    A function that gets the ram from a system
    and returns it to the user.

    function used:
    - virtual_memory
    """
    return psutil.virtual_memory().available
def get_sys_info():
    """
    A function that gets the following information
    and then returns them to the user to view:
    - hostname
    - addresses
    """
    hostname = socket.gethostname
    address_info = []
    sys_addresses = socket.getaddrinfo(socket.gethostname(), None)
    for address in sys_addresses:
        address_info.append((address[0].name, address[4][0]))
def load_sys():
    return psutil.cpu_percent(interval=0.2)
def show_version():
    """
    A function that prints out system version information.
    """
    sys_version = sys.version_info
    return sys_version
def show_sensors():
    """
    A method that will show the sensor on a system.
    """
    print("Python version: {0.major}.{0.minor}".format(show_version()))
    for address in get_sys_info():
        print("IP addresses: {0[1]} ({0[0]})".format(address))
    print("CPU Load: {.1f}".format(load_sys()))
    print("RAM Available: {} MiB".format(get_ram() / 1024**2))
    print("AC Connected: {}".format(check_power()))

################## ---------------------- Ending adding functions. ---------------------- ##################


#Using the ifmain construct.
if __name__ == '__main__':
    command_line(sys.argv)
