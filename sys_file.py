#!/usr/bin/env python
# coding: utf-8

#The first line defines the interpreter and the second line defines the encoding for the project.
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

def show_version(user_input):
    """
    A function that prints out system version information.
    """
    sys_version = sys.version_info
    for line in sys_version:
        print(line)
def get_sys_info():
    """
    A function that gets the following information
    and then returns them to the user to view:
    - hostname
    - addresses
    """
    hostname = socket.gethostname
print(HELP_TEXT)