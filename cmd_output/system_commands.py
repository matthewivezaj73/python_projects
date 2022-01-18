#Importing libraries.
from datetime import datetime
import os
import subprocess
from datetime import date
#Subprocess allow us to send command line commands to windows through python.
#(We do this so that we can piggyback multiple commands.  It allows us to save time typing.  
# We can also be clever and only output what we are interested in, 
# instead of sifting through unessential information.  Don’t work harder, work smarter.)
output = subprocess.Popen(['netstat','-ano'],stdout=subprocess.PIPE).communicate()
#Grabbing the current time.
now=datetime.datetime.now()
"""
i.	output – variable we are instantiating.  
ii.	subprocess – calls the subprocess module
iii.	Popen – calls a subroutine defined in subprocess
iv.	[‘netstat’, ‘-ano’] – We are feeding the command netstat as text into Popen with the arguments ‘-ano’.  If we only wanted to send netstat by itself as default, we would have ‘netstat’ with no brackets.  
v.	stdout=subprocess.PIPE – We are sending the output back to this call for connection to the variable. 
"""
# #Printing output 
# print(output)
#Checking the type of the
type(output)
#Setting new line breaks so that the data comes out all clean.
new_lines = output[0].split('\r\n  '.encode())
my_date = date.today()
today = my_date.strftime("%B %d, %Y")
#Opening the parent text file.
with open("text_files/my_output.txt") as text_file:
    #Checking if the file already exists.
    if os.path.isfile("text_files/my_CSV_output.csv"):
        #Asking the user if they would like to overwrite the file.
        my_question = input("the file already exists, would you like to overwrite it?\nPlease respond with Y/N for yes(Y) and no(N) respectively: ")
        #Creating a child csv file.
        with open("text_files/my_CSV_output.csv","w") as Exists_csv_output:
            #Creating a for loop.
            for line in new_lines:
                #Checking if the line is equal to establised
                if line.find("ESTABLISHED".encode()):
                    print(line)
                    line = str(line).encode()
                    Exists_csv_output.write(str(line)+" "+ today)
                    Exists_csv_output.write("")
    #Handling the case where the file does not exist in the text_files directory.
    elif not os.path.isfile("text_files/my_CSV_output.csv"):

        #Creating a child csv file.
        with open("text_files/my_CSV_output.csv","w+") as csv_output:
            read_output = csv_output.readlines()
            csv_output.write("ESTABLISHED"+" "+ today)
            #print(len(read_output))
            #Creating a for loop.
            for line in new_lines:#
                #Checking if the line is equal to establised
                if line.find("ESTABLISHED".encode()):
                    print(line)
                    my_line = "ESTABLISHED".encode()
                    csv_output.write(str(line)+"\n")
                    csv_output.write("")
                if line.find("Foreign".encode()):
                    print(line)
                    my_line = "Foreign".encode()
                    csv_output.write(str(line)+"\n")
                    csv_output.write("")
                else:
                    continue
            csv_output.write("\n")
                