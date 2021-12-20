#Importing libraries.
import click
import os
import socket
import sys
import argparse
import psutil
#Creating functions.
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
def show_arg(argv):
    parser = argparse.ArgumentParser(
        description='Displays the values of the sensors',
        add_help=True,
    )
    arguments = parser.parse_args()
    show_sensors()
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
#Adding a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user to enter a choice.
    do_something = input("Please enter \'csv\' if you would like to create a csv file.\n\n")
    #Handling the case where the user enters csv.
    if do_something.lower() == "csv":
        #Creating a blank list.
        csv_content_list = []
        #Setting a flag.
        not_list = False
        #Creating a while loop.
        while not not_list:
            #Printing directions to the user.
            print("Each line you add will be applied to a column in the table")
            #Giving the user a choice of what to do.
            user_choice = input("Enter 1 to enter a value in the csv file.\n\nEnter 2 to read each line in the csv file.\n\nEnter 3 to edit a line in the csv file.\n\n")
            #Handling case 1.
            if user_choice == "1":
                #Asking the user to input text.
                content = input("Please enter the text that you would like to enter into the csv file for the first row: ")
            
                #Printing out a line to tell the user that we are processing their csv file.
                click.echo("processing your csv file...")
                #Opening a file for reading.
                with open("text_files/click_output.txt") as output_txt:
                    #Assigning a file path to a variable.
                    csv_file = "text_files/click_output.csv"
                    #Handling case where the file does not exist.
                    if os.ispath(csv_file):
                            
                        #Creating a csv file for writing.
                        with open("text_files/click_output.csv","w+") as csv_output:
                            csv_output.write(content)