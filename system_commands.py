#Importing libraries.
import os
import subprocess
#Subprocess allow us to send command line commands to windows through python.
#(We do this so that we can piggyback multiple commands.  It allows us to save time typing.  
# We can also be clever and only output what we are interested in, 
# instead of sifting through unessential information.  Don’t work harder, work smarter.)
output = subprocess.Popen(['netstat','-ano'],stdout=subprocess.PIPE).commmunicate()
"""
i.	output – variable we are instantiating.  
ii.	subprocess – calls the subprocess module
iii.	Popen – calls a subroutine defined in subprocess
iv.	[‘netstat’, ‘-ano’] – We are feeding the command netstat as text into Popen with the arguments ‘-ano’.  If we only wanted to send netstat by itself as default, we would have ‘netstat’ with no brackets.  
v.	stdout=subprocess.PIPE – We are sending the output back to this call for connection to the variable. 
"""