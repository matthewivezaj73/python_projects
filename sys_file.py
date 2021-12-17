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
HELP_TEXT = """usage: python {program_name:s}
Displays the values of the sensors
Options and arguments:
--help:    Display this message"""

def check_power():
    """
    A function that checks to 
    see if the power is connected on a system.

    Function used:
    - sensors_battery
    """
    return psutil.sensors_battery().power_plugged
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
    print(hostname)
    sys_addresses = socket.getaddrinfo(socket.gethostname(), None)
    for address in sys_addresses:
        print(address)
def load_sys():
    return psutil.cpu_percent(interval=0.2)
def show_version(user_input):
    """
    A function that prints out system version information.
    """
    sys_version = sys.version_info
    for line in sys_version:
        print(line)
print(HELP_TEXT)
#Using the ifmain construct.
if __name__ == '__main__':
    sys_info = get_sys_info()
