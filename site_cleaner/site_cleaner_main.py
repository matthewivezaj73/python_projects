#Importing the library.
from os import read
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "text_files/site_text.txt"
#Importing class.
#Creating an instance of a class.
#Reading the conents of the site.
read_site = urlopen("https://tradingeconomics.com/calendar#")
with open("")
for line in read_site:
    print(line)
#Creating a blank list.
website_arr = []
#Adding a flag.
not_done = False
#Asking the user what they would like to do.
while not not_done:
    #Asking the user what they would like to do.
    user_choice = input("Please enter c if you would like to clean up the text from the site.\nPlease enter d to display the content from the scraped site.\nPlease enter e to exit:")
    #Handling the case where the user enters c.
    if user_choice.lower() == "c":
        #Creating a for loop.
        for line in read_site:
            #Cleaning up each line.
            line = str(line).replace("b'","").replace("b\"","").replace('\/',"")
            line = line.replace("\n'","")
            if "\n" in line:
                line = line.remove[-1]
            line = str(line).replace("\ ","")
            #Appending each line to the list.
            website_arr.append(line)
    #Handling the case where the user enters d.
    elif user_choice.lower() == "d":
        #For loop to print the lines from the original text.
        for line in website_arr:

            print(line)

