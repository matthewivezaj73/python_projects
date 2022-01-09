#Importing the library.
from os import read
from urllib.request import urlopen
#Assinging a variable to the path of the text file.
my_file = "text_files/site_text.txt"
#Importing class.
from classes.scraping_validator import ScrapingValidator
#Creating an instance of a class.
my_site_scraper = ScrapingValidator("https://www.google.com/",23)
#Setting a flag.
not_scraped = False
#Testing for input from the user.
while not not_scraped:
    #Asking the user what they want to do.
    user_choice = input("Please enter \'r\' if you would like to read the contents of a website.\n\nPlease enter \'csv\' if you would like to read the contents of the csv file.\n\nPlease enter \'rem\' if you would like to remove characters from the csv.")
    #Handling the case where the user enters r.
    if user_choice.lower() == "r":
        #Setting a flag.
        not_site_entered = False
        #Testing to ensure the data is ok.
        while not not_site_entered:
            #Asking for input from the user.
            site_entered = input("Please enter the name of a site whose data you would like scraped or \'q\' to quit: ")
            #Handling the case where the user enters q.
            if site_entered.lower() == "q":
                not_site_entered = True
            #Creating a variable that grabs the text from a site.
            read_site = urlopen(site_entered)
            #Creating a blank list.
            my_list = []
            for line in read_site:
                #Appending each line along with "," to the list.
                my_list.append(str(line)+",")             
            #Opening the text file to work with.
            with open(my_file) as fold:

                with open("text_files/site_text.csv","w+") as fawn:
                    # Going through each line in the list.
                    for line in my_list:
                        #Writing each line to the file.
                        fawn.write(str(line))
    #Handling the case where the user wants to read the contents of the csv file.
    elif user_choice.lower() == "csv":
        with open("text_files/site_text.csv") as fawn:
            # Going through each line in the list.
            for line in fawn:
                #Writing each line to the file.
                print(line)
    #Handling the case where the user wants to remove a character from the csv file.
    elif user_choice.lower() == "rem":
        #Asking the user what character they would like to remove.
        char_remove = input("Please enter a character that you would like to remove: ")
        #Opening the file for reading.
        with open("text_files/site_text.csv","r") as fawn:
            read_lines = fawn.readlines()
            for line in read_lines:
                line = line.replace(char_remove,"")
                print(line)
