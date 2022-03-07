#Importing library
import socket
# Begin checking for all open ports.
open_ports = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Checking on the local host.
result = open_ports.connect_ex(('127.0.0.1', 3306))
#Checking for open ports.
if result == 0:
    print('socket is open')
