#Importing libraries.
import click
import os
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
            #Asking the user to input text.
            content = input("Please enter the text that you would like to enter into the csv file for the first row: ")
            #Handling the case where the user would like to add content to the list.
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