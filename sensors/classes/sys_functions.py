#Importing libs.
import socket
import sys
import argparse
import psutil
import click
class Temperature()
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
        click.echo("The ac adapter is connected.")
    else:
        click.echo("The ac adapter is not connected.")
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
            click.echo(HELP_TEXT.format(program_name=program_name))
            return
    except ValueError:
        click.echo("Unknown arguments {}".format(arguments))
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
    click.echo("Python version: {0.major}.{0.minor}".format(python_version()))
    for address in ip_addresses():
        click.secho(f"IP addresses: {address})")
    click.echo(f"CPU Load: {cpu_load()}")
    click.echo("RAM Available: {} MiB".format(ram_available() / 1024**2))