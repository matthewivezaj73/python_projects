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
    print(sys.version_info)
def get_sys_info():
    
print(HELP_TEXT)